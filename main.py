import logging
import time
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

# System Settings
BASE_PREMIUM = 1000

# Logging Setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Driving Data Clustering
class PatternClusterer:
    def cluster(self, df):
        X = df[['speed', 'hard_brakes']].values
        kmeans = KMeans(n_clusters=2, random_state=42)
        df['pattern_group'] = kmeans.fit_predict(X)
        logging.info("Clustered driving patterns in dataset.")
        return df

# Risk Adjustment for Road Conditions
class RiskAdjuster:
    def apply_conditions(self, score, weather, traffic):
        if weather.lower() in ['rain', 'snow', 'fog']:
            score += 10
        if traffic.lower() == 'heavy':
            score += 5
        return min(score, 100)

# Real-Time Data Handler
class DataStreamHandler:
    def process(self, trips):
        processed_trips = []
        for packet in trips:
          
            if np.random.random() < 0.1:
                logging.warning("Simulated device failure: Skipping invalid packet.")
                continue
            logging.info(f"Received data: {packet}")
            processed_trips.append(packet)
            time.sleep(0.5) 
        return processed_trips

# Collect Trip Info
def collect_trip_info():
    print("\nEnter your trip details:")
    driver_name = input("Driver Name: ").strip()
    license_number = input("License Number: ").strip()

    while True:
        try:
            speed = int(input("Average Speed (km/h): ").strip())
            if speed < 0:
                raise ValueError("Speed cannot be negative.")
            break
        except ValueError:
            print("Enter a valid number for speed.")

    while True:
        try:
            hard_brakes = int(input("Number of Hard Braking Events: ").strip())
            if hard_brakes < 0:
                raise ValueError("Hard brakes cannot be negative.")
            break
        except ValueError:
            print("Enter a valid number for hard brakes.")

    weather = input("Weather Condition (Clear, Rain, Snow, Fog): ").strip()
    traffic = input("Traffic Condition (Light, Moderate, Heavy): ").strip()

    data = {
        'driver_name': driver_name,
        'license_number': license_number,
        'speed': speed,
        'hard_brakes': hard_brakes,
        'weather': weather,
        'traffic': traffic,
        'timestamp': time.time()
    }
    logging.info(f"Collected trip data: {data}")
    return data

# Remove Personal Info
def remove_personal_info(data: dict) -> dict:
    data.pop('driver_name', None)
    data.pop('license_number', None)
    logging.info(f"Data after removing personal info: {data}")
    return data

# Evaluate Driving
def evaluate_driving(data: dict) -> dict:
    over_speed = data['speed'] > 80
    many_brakes = data['hard_brakes'] > 2
    data['risky'] = over_speed or many_brakes
    logging.info(f"Driving evaluation: Over Speed={over_speed}, Hard Brakes={many_brakes}")
    return data

# Compute Risk Score
def compute_risk(data: dict, cluster_group: int) -> float:
    speed_score = data['speed'] * 0.1
    brake_score = data['hard_brakes'] * 5
    risk = min(speed_score + brake_score, 100)

    # Adjust risk based on cluster group (0: safe, 1: risky)
    risk *= 1.0 if cluster_group == 0 else 1.2
    logging.info(f"Risk after cluster adjustment: {risk:.2f}")

    adjuster = RiskAdjuster()
    risk = adjuster.apply_conditions(risk, data['weather'], data['traffic'])

    logging.info(f"Final risk score: {risk:.2f}")
    return risk

# Calculate Premium
def calculate_premium(risk: float) -> float:
    if risk > 70:
        premium = BASE_PREMIUM * 1.2
    elif risk < 30:
        premium = BASE_PREMIUM * 0.9
    else:
        premium = BASE_PREMIUM
    logging.info(f"Premium set to: ${premium:.2f}")
    return premium

# Give Driver Advice
def driver_advice(risk: float) -> str:
    if risk > 70:
        msg = "Risk detected! Drive safer to lower your premium."
    elif risk < 30:
        msg = "Excellent driving! You earned a safe driver discount."
    else:
        msg = "Keep it steady! Maintain safe driving to keep your rates stable."
    logging.info(f"Advice: {msg}")
    return msg

# Workflow
def main():
    # Collect multiple trips to simulate a data stream
    trips = []
    while True:
        trip = collect_trip_info()
        trips.append(trip)
        more = input("Add another trip? (y/n): ").strip().lower()
        if more != 'y':
            break

    # Process trips as a stream
    stream_handler = DataStreamHandler()
    processed_trips = stream_handler.process(trips)

    if not processed_trips:
        print("No valid trip data received. Exiting.")
        return

    # Cluster trips to identify patterns
    anonymized_trips = [remove_personal_info(trip.copy()) for trip in processed_trips]
    df = pd.DataFrame(anonymized_trips)
    clusterer = PatternClusterer()
    clustered_df = clusterer.cluster(df)

    # Evaluate and compute risk for each trip
    risk_scores = []
    for idx, trip in clustered_df.iterrows():
        evaluated = evaluate_driving(trip.to_dict())
        risk_score = compute_risk(evaluated, trip['pattern_group'])
        risk_scores.append(risk_score)

    # Average risk score for premium calculation
    avg_risk = np.mean(risk_scores)
    premium = calculate_premium(avg_risk)
    advice = driver_advice(avg_risk)

    print("\n==== Insurance Summary ====")
    print(f"Processed {len(processed_trips)} trips")
    print(f"Average Risk Score: {avg_risk:.2f}")
    print(f"Premium: ${premium:.2f}")
    print(f"Advice: {advice}")
    print("==========================\n")

# Entry
if __name__ == "__main__":
    while True:
        main()
        again = input("Run again? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye! Drive safe!")
            break
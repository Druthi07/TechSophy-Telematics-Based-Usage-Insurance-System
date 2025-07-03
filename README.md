Introduction
This project is a simple Python program that calculates insurance premiums based on driving data. It features clustering, risk scoring, and real-time data processing.

Requirements
Python 3.x
Required libraries:
numpy
pandas
scikit-learn

To install dependencies, run:
bash
pip install numpy pandas scikit-learn

How to Use
Run the Code
In your terminal, execute:

bash
python <filename>.py

Enter Trip Details
Driver Name
License Number
Average Speed (km/h)
Number of Hard Braking Events
Weather Condition (Clear, Rain, Snow, Fog)
Traffic Condition (Light, Moderate, Heavy)

Add Multiple Trips
After each trip, you’ll be asked if you want to add another trip.

View Results
Number of processed trips
Average risk score
Premium amount
Advice for the driver

Key Features
Driving Pattern Clustering:
Uses KMeans algorithm to group driving patterns into two clusters (Safe/Risky).
Risk Scoring:
Calculates risk score based on speed, hard brakes, weather, and traffic.
Premium Calculation:
Adjusts insurance premium based on the risk score.
Data Anonymization:
Removes personal information (name, license number) before processing.
Real-Time Data Handling:
Processes each trip as a data stream.

Notes
This program is for demo purposes only.


Drive safely!

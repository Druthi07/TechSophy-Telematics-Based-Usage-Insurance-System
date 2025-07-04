## Requirements

- Python 3.x
- Required libraries:
  - numpy
  - pandas
  - scikit-learn

## How to Use

- Run the code:
  - In your terminal, execute:
    ```
    python <filename>.py
    ```
- Enter trip details:
  - Driver Name
  - License Number
  - Average Speed (km/h)
  - Number of Hard Braking Events
  - Weather Condition (Clear, Rain, Snow, Fog)
  - Traffic Condition (Light, Moderate, Heavy)
- Add multiple trips (you’ll be asked after each trip)
- **Minimum two trips are required** for pattern clustering and premium calculation. 
- View results:
  - Number of processed trips
  - Average risk score
  - Premium amount
  - Advice for the driver


## Key Features

- Driving Pattern Clustering:
  - Uses the KMeans algorithm to group driving patterns into two clusters (Safe/Risky).

- Risk Scoring:
  - Calculates risk score based on speed, hard brakes, weather, and traffic.

- Premium Calculation:
  - Adjusts insurance premium based on the risk score.

- Data Anonymization:
  - Removes personal information (name, license number) before processing.

- Real-Time Data Handling:
  - Processes each trip as a data stream.
 
## Docker Usage

To build and run the system inside Docker:

1. Build the Docker image:
docker build -t telematics-insurance .

2. Run the container:
docker run -it telematics-insurance

3. To persist files or logs from the container to your local machine:
docker run -it -v ${PWD}:/app telematics-insurance
## Notes

- This program is for demo purposes only.

# Sensor Data Anomaly Detector

This project implements an anomaly detection system using Isolation Forest algorithm on time-series sensor data.

## Features

* Generates synthetic time-series sensor data for demonstration purposes.
* Utilizes Scikit-learn's Isolation Forest algorithm to detect anomalies in the data.
* Evaluates model performance using accuracy score.

## Setup and Run Instructions

1. Clone this repository: `git clone https://github.com/your-github-username/anomaly-detection-in-sensor-data.git`
2. Install required packages: `pip install -r requirements.txt`
3. Run the script: `python main.py`

## Sample Output

| timestamp | sensor1 | sensor2 | prediction |
| --- | --- | --- | --- |
| 2022-01-01 00:00:00 | 9.5 | 19.8 | -1 |
| 2022-01-01 00:05:00 | 11.2 | 21.3 | 1 |

## What I Learned

During the development of this project, I learned about the importance of contamination parameter in Isolation Forest algorithm and its impact on model performance. I also gained experience with generating synthetic data for demonstration purposes and evaluating machine learning model accuracy using metrics like accuracy score. This project helped me solidify my understanding of anomaly detection techniques and their applications in real-world scenarios.
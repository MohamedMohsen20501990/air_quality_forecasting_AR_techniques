This project analyzes low-cost air quality sensor data from the sensors.AFRICA Air Quality Archive for Nairobi. The dataset contains time-series measurements of particulate matter (PM), temperature, and humidity collected from distributed environmental sensors.

The goal is to explore air pollution patterns over time, understand environmental influences, and study the behavior of low-cost air quality sensors.

📊 Dataset Overview

The dataset includes environmental readings collected using low-cost sensors deployed in different locations. It is stored in CSV format and contains time-stamped measurements.

🌫️ Measured Variables
Variable	Meaning
P0	PM1 (particles ≤ 1 µm)
P1	PM10 (particles ≤ 10 µm)
P2	PM2.5 (particles ≤ 2.5 µm)
Temperature	Ambient temperature (°C)
Humidity	Relative humidity (%)
📌 Other Fields
Column	Description
sensor_id	Unique sensor identifier
sensor_type	Type of sensor (e.g., SDS011, DHT22)
location	Location ID of sensor
lat, lon	Geographic coordinates
timestamp	Date and time of measurement
value_type	Type of measurement recorded
value	Numeric sensor reading
🎯 Project Objectives

This project focuses on:

📈 Exploring air quality trends over time
🌫️ Analyzing particulate matter behavior (PM1, PM2.5, PM10)
🌡️ Studying relationships between weather and pollution
🕒 Understanding temporal patterns (hourly/daily/seasonal)
🚨 Detecting pollution spikes and anomalies
📍 Comparing air quality across sensor locations
🧹 Data Processing Workflow

The analysis pipeline includes:

Loading raw CSV sensor data
Removing duplicate or malformed header rows
Parsing timestamps into datetime objects
Converting measurement values to numeric format
Reshaping data from long to wide format (pivoting by value_type)
Resampling time series for trend analysis (hourly → daily averages)
📊 Exploratory Data Analysis (EDA)

The notebook performs:

Time-series visualization of PM2.5 and PM10
Rolling mean smoothing for trend detection
Seasonal decomposition of air pollution patterns
Correlation analysis between temperature, humidity, and PM levels
Detection of high pollution events.
Download data using this link "https://open.africa/dataset/sensorsafrica-airquality-archive-nairobi"

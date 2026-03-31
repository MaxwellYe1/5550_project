# Short-Term Forecasting of Extreme Heat Events in Virginia

## Project Overview

This project builds an end-to-end machine learning pipeline to forecast short-term extreme heat events using historical daily climate data from a weather station in Virginia.

Instead of detecting heatwaves based on current temperature thresholds, this project focuses on predicting whether a heatwave will begin within the next three days.

---

## Data Source

* NOAA Global Historical Climatology Network (GHCN) Daily dataset
* Station: Abingdon 3 S, Virginia (USC00440021)
* Time range: 2000–2024

Key variables used:

* Temperature: TMAX, TMIN
* Precipitation: PRCP
* Snow: SNOW, SNWD
* Weather indicators: WTxx

---

## Project Structure

```
project/
│
├── data_cleaning.py          # Clean raw climate data and save processed CSV
├── heatwave_model.ipynb         # Feature engineering, modeling, and evaluation
│
├── climate_data.csv          # Raw dataset
├── cleaned_climate_data.csv  # Cleaned dataset
├── emissions.csv             # My carbon tracking
│
├── outputs/                  # Model outputs (predictions, feature importance)
│
└── README.md
```

---

## Methodology

### 1. Data Cleaning

* Parse and standardize date format
* Convert numeric variables
* Handle missing values
* Convert weather indicators (WTxx) to binary

### 2. Heatwave Definition

A heatwave is defined as:

* ≥ 3 consecutive days
* TMAX exceeds the 95th percentile of summer temperatures

### 3. Target Construction

For each day *t*, the target variable is:

* 1 → A heatwave begins within the next 3 days
* 0 → Otherwise

This ensures a forward-looking prediction task.

---

## Feature Engineering

Features are constructed using only past and current information:

* Lag features (e.g., TMAX_LAG1, TMIN_LAG1)
* Rolling statistics (3-day, 5-day averages)
* Temperature trends (daily differences)
* Seasonal encoding (month and day-of-year)
* Recent hot-day counts

---

## Models

The following models are implemented using scikit-learn:

* Logistic Regression (baseline)
* Random Forest

---

## Evaluation

Due to class imbalance, the following metrics are used:

* Precision
* Recall
* F1-score
* ROC-AUC
* Confusion Matrix

A simple baseline (predicting no heatwave) is also included for comparison.

---

## Carbon Cost Tracking

The project uses CodeCarbon to estimate:

* Energy consumption
* Carbon emissions

This helps evaluate the environmental impact of the machine learning process.

---


## Output

The pipeline generates:

* Cleaned dataset
* Model predictions (CSV)
* Feature importance (Random Forest)
* Evaluation metrics (printed in console)

---

## Notes

* The focus is on functionality rather than optimization.
* Future work may include multi-station modeling and advanced time-series methods.

---

## Author

Liming Ye
Georgetown University – Data Science & Analytics
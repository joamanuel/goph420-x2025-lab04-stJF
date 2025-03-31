# goph420-x2025-lab0-stJF

GOPH 420/699 – Inv. and Param. Est. for Geoph. (W2025)

Lab Assignment #4

Linear Least Squares Regression

# Lab 04 – Gutenberg-Richter Regression Analysis

This project implements a multiple linear regression approach to analyze microseismic data using the Gutenberg-Richter law. The goal is to estimate the parameters \( a \) and \( b \) that describe the frequency-magnitude relationship of earthquakes, and to investigate how these parameters change over different time intervals within a seismic dataset.

## 📊 Objective

- Apply least squares regression to the linearized Gutenberg-Richter law.
- Analyze how the \( b \)-value varies over time.
- Compare seismicity across multiple operational periods (e.g., during fluid injection).


## 🚀 How to Run

1. Clone the repo and navigate to the `examples/` folder.
2. Ensure you have Python ≥ 3.8 installed.
3. Install dependencies:
   ```bash
   pip install -r ../requirements.txt

## Run the main analysis
   python driver.py


## 📈 Outputs

- Plot of magnitude vs. time for the full dataset
- Separate plots of $\log_{10}(N)$ vs. $M$ for selected time intervals
- Estimated parameters $a$, $b$, and $R^2$ printed to the console for each interval
- All figures saved to the `figures/` directory, including:
  - `period_A.png`
  - `period_B.png`
  - `period_C.png`
  - `gr_comparison_all_periods.png`



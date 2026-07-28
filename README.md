# AltScore Credit Scoring Dashboard & ML Engine

A full-stack, real-time credit scoring dashboard and machine learning decision engine built with FastAPI, LightGBM/XGBoost, and HTML5/Vanilla JS — transforming static credit scoring models into transparent, explainable "glass-box" AI systems.

## Overview

This directory contains the production codebase, execution scripts, and analytical notebooks for **AltScore Zenith**. Traditional credit risk models are built on static statistical profiles that are hard to audit, leading to cold-start problems and algorithmic bias. This project implements a fully explainable credit decision intelligence platform powered by an ensemble-based **LightGBM** classifier. 

It manages the entire lifecycle: raw database preprocessing, complex feature aggregation (integrating installments, POS balances, and bureau datasets), real-time FastAPI endpoints, and a responsive HTML5 dashboard. To maximize user experience and decrease data-entry barriers, a backend auto-imputation pipeline allows users to input just 20 key fields on the dashboard, dynamically reconstructs the full 244-dimensional feature vector, and scores it instantly. Results are accompanied by diagnostic positive/negative impact drivers and counterfactual guidelines to assist rejected applicants.

---

## 🚀 The Three Novelties

This project implements three key machine learning novelties developed across research phases:

### 1. Financial Trajectory Feature Engineering (by Muskan)
Calculates **5 dynamic trajectory variables** using historical installment payment records to see if repayment behavior is improving or declining over time:
*   `TRAJECTORY_EARLY_LATE_RATE`: Late-payment rate in the early history.
*   `TRAJECTORY_RECENT_LATE_RATE`: Late-payment rate in the recent half of history.
*   `TRAJECTORY_SLOPE`: Repayment trend regression slope.
*   `TRAJECTORY_IMPROVEMENT`: Flag for declining late-payment rates.
*   `TRAJECTORY_SCORE`: Dynamic score based on repayment trajectory.

### 2. Counterfactual Explanations for XAI (by Nithilan)
Calculates the **minimum feature changes required** to flip a decision from *Rejected* to *Approved*. 
*   It utilizes a **Feature Actionability Map** classifying inputs by difficulty (Immutable, Hard, Medium, Easy, Very Easy) to suggest realistic actions.

### 3. Fairness Analysis & Bias Auditing (by Charumadhi)
Audits predictions across **5 protected attributes** (Gender, Age, Income, Region, Credit History) using **4 metrics** (Disparate Impact Ratio, Statistical Parity Difference, Equal Opportunity Difference, Average Odds Difference) to ensure strict ethical lending compliance.

---

## Features

- **Real-Time LightGBM Inference** — default risk prediction.
- **Explainable AI (XAI)** — local positive/negative risk impact factors.
- **Actionable Counterfactuals** — suggestions for rejected applicants.
- **Auto-Imputation Pipeline** — reconstructs 244-dimensional arrays from 20 UI inputs.
- **Dark-Theme Glassmorphic UI** — animated gauge and metrics indicators.

---

## Tech Stack

*   **Backend**: Python, FastAPI, Uvicorn, Pydantic, joblib
*   **ML Engines**: LightGBM, XGBoost, Scikit-Learn, Pandas, NumPy
*   **Frontend**: HTML5, Vanilla JS, Custom CSS (CSS variables, Flexbox)

---

## Running Locally

### Prerequisites
- Python 3.8+

### Automated (Windows)
```cmd
start_dashboard.bat
```

### Manual
1.  **Start FastAPI Backend**:
    ```bash
    pip install -r requirements.txt
    python app.py
    ```
    *API will run on `http://127.0.0.1:8001`*
2.  **Start Web Frontend**:
    ```bash
    cd frontend
    python -m http.server 8080
    ```
    *Access dashboard at `http://localhost:8080`*

---

## API Summary

| Method | Endpoint | Description |
|---|---|---|
| POST | `/predict` | Ingests 20 inputs, auto-imputes missing, returns decision and confidence score |
| POST | `/explain` | Returns positive/negative decision factors and counterfactual tips |
| GET | `/docs` | Interactive Swagger UI docs |

---

## Author

Charumadhi M
[LinkedIn](https://www.linkedin.com/in/charumadhi-m-a5247a329/) · [GitHub](https://github.com/charumadhi-sudo)

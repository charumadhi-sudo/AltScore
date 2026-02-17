# AltScore - Alternative Credit Scoring System

<div align="center">

**Making Credit Access Fair for Everyone**

*An AI-powered alternative credit scoring system using transaction history, utility payment proxies, and social data to predict creditworthiness for underbanked populations.*

</div>

---

##  Table of Contents

- [About The Project](#about-the-project)
- [Problem Statement](#problem-statement)
- [Our Solution](#our-solution)
- [Key Findings](#key-findings)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [Roadmap](#roadmap)
- [Technologies Used](#technologies-used)
- [Team](#team)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

##  About The Project

**AltScore** is an alternative credit scoring system designed for the **Zenith Hackathon 5.0** that uses non-traditional data sources to predict creditworthiness. Unlike traditional credit scoring that requires credit history, our model leverages:

-  **Transaction history** - Payment patterns and spending behavior
-  **Utility payment proxy** - POS/Cash balance records showing financial discipline
-  **Social indicators** - Geographic, demographic, and community context

### Why This Matters

**1.7 billion adults worldwide** lack access to formal financial services because they have no traditional credit history. AltScore aims to change that.

---

##  Problem Statement

### The Credit Access Gap

Imagine you're 25 years old. You've been responsibly paying rent, utilities, and phone bills for years. You've never missed a payment. But when you walk into a bank for a small loan, they say **no**.

**Why?** Because you have no "credit history."

### Traditional Credit Scoring Fails Because It Requires:

❌ Previous loans (which you don't have)  
❌ Credit cards (which you couldn't get without credit history)  
❌ Collateral (which young people rarely have)  

**The Catch-22:** You need credit to build credit.

---

##  Our Solution

### Alternative Data Approach

Instead of asking *"Do you have credit history?"*, we ask:

 Do you pay your bills on time?  
 Are you consistent with payments?  
 What's your life context - age, education, where you live?  
 How do you behave with money over time?  

### Three-Layer Data Strategy
```
┌─────────────────────────────────────────┐
│ LAYER 1: Transaction History           │
│ • 13.6M installment payment records     │
│ • 3.8M credit card transactions         │
│ • Payment timing, amounts, regularity   │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ LAYER 2: Utility Payment Proxy         │
│ • 10M POS/Cash balance records          │
│ • 68.4% pay EARLY (not just on-time!)  │
│ • Shows financial discipline            │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ LAYER 3: Social & Network Data         │
│ • 1.7M bureau credit relationships      │
│ • Geographic community indicators       │
│ • Demographic life stage signals        │
└─────────────────────────────────────────┘
```

---

##  Key Findings

###  Major Discoveries from Week 1 Analysis

| Finding | Impact | Significance |
|---------|--------|--------------|
| **Alternative Data Effectiveness** | **21% reduction** in default risk | Validates our entire approach ✅ |
| **Payment Behavior** | **68.4%** pay early | Excellent proxy for financial discipline |
| **Top Predictor** | EXT_SOURCE_3 (0.179 correlation) | Alternative scores beat traditional metrics |
| **Target Segment** | 2,470 (0.8%) have NO data | Underbanked population we can serve |
| **Data Richness** | 58.4M records across 6 tables | Robust feature engineering potential |

### 📊 Statistical Validation
```python
# Default Rate by Alternative Data Availability
NO alternative data:    7.25% default (2,470 people)
Only bureau history:    5.72% default (21% LOWER! ✓)
Only previous apps:    10.16% default 
Both sources:           7.84% default
```

**Conclusion:** Alternative data sources **DO predict creditworthiness** and reduce risk.

---

## 📁 Dataset

### Home Credit Default Risk

**Source:** [Kaggle Competition](https://www.kaggle.com/c/home-credit-default-risk)

#### Main Application Data
- **307,511 loan applications** with outcomes (who repaid, who defaulted)
- **122 features** including demographics, financials, and target variable
- **8.07% default rate** (24,825 defaults)

#### Supplementary Data Tables

| Dataset | Records | Purpose | Coverage |
|---------|---------|---------|----------|
| **bureau.csv** | 1,716,428 | Credit history from other institutions | 99.4% of applications |
| **bureau_balance.csv** | 27,299,925 | Monthly credit behavior patterns | Historical depth |
| **previous_application.csv** | 1,670,214 | Past loan application history | 110.2% (multiple per person) |
| **POS_CASH_balance.csv** | 10,001,358 | Recurring payment behavior (utility proxy) ⭐ | 304.5% |
| **credit_card_balance.csv** | 3,840,312 | Card usage & payment patterns | 33.9% |
| **installments_payments.csv** | 13,605,401 | Payment timing & amount behavior | 324.5% |

**Total:** 58,441,149 records across all tables

### Data Quality Challenges

- ⚠️ **67 features** have missing values (54% of features)
- ⚠️ **41 features** have >50% missing data
- ✅ Strategy: MICE imputation + missingness flags

---

## 📂 Project Structure
```
AltScore/
│
├── data/                          # Dataset files (not tracked in git)
│   ├── application_train.csv
│   ├── bureau.csv
│   ├── bureau_balance.csv
│   ├── previous_application.csv
│   ├── POS_CASH_balance.csv
│   ├── credit_card_balance.csv
│   ├── installments_payments.csv
│   └── HomeCredit_columns_description.csv
│
├── notebooks/                     # Jupyter notebooks
│   ├── 01_data_exploration.ipynb       # Day 1: Data profiling
│   ├── 02_eda_analysis.ipynb          # Day 2: Visual exploration
│   └── 03_feature_engineering.ipynb   # Day 3: Feature creation (upcoming)
│
├── src/                          # Source code
│   ├── __init__.py
│   ├── data_loader.py            # Data loading utilities
│   ├── preprocessing.py          # Data cleaning & preprocessing
│   ├── feature_engineering.py    # Feature creation functions
│   ├── models.py                 # Model training & evaluation
│   └── utils.py                  # Helper functions
│
├── visualizations/               # Generated charts (10 total)
│   ├── 01_target_distribution.png
│   ├── 02_demographic_analysis.png
│   ├── 03_financial_features.png
│   ├── 04_correlation_heatmap.png
│   ├── 05_alternative_data_insights.png
│   ├── 06_geographic_analysis.png
│   ├── 07_missing_values_analysis.png
│   ├── 08_external_source_analysis.png
│   ├── 09_feature_importance_preview.png
│   └── 10_payment_behavior_analysis.png
│
├── reports/                      # Analysis reports (12 files)
│   ├── column_descriptions.csv
│   ├── target_distribution.csv
│   ├── datasets_summary.csv
│   ├── data_coverage.csv
│   ├── missing_values_analysis.csv
│   ├── statistical_summary.csv
│   └── eda_insights_comprehensive.txt
│
├── models/                       # Trained models (upcoming)
│   └── baseline_xgboost.pkl
│
├── presentation/                 # Review presentations
│   └── Review1_AltScore.pdf
│
├── .gitignore                    # Git ignore file
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── LICENSE                       # MIT License
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook (for running .ipynb files)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Nithilan77/AltScore.git
cd AltScore
```

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download the dataset**

Option A: Using Kaggle CLI
```bash
pip install kaggle
kaggle competitions download -c home-credit-default-risk
unzip home-credit-default-risk.zip -d data/
```

Option B: Manual download
- Visit [Kaggle Competition](https://www.kaggle.com/c/home-credit-default-risk/data)
- Download all CSV files
- Place in `data/` folder

5. **Verify installation**
```bash
python -c "import pandas, numpy, sklearn, xgboost; print('All dependencies installed!')"
```

---

## 💻 Usage

### Running the Analysis

#### Step 1: Data Exploration
```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```

**What it does:**
- Loads all 7 datasets (307K applications + 58M supplementary records)
- Profiles data quality and missing values
- Analyzes target distribution (8.07% default rate)
- Generates 10 detailed reports

**Output:** `reports/` folder with CSV summaries

#### Step 2: EDA & Visualization
```bash
jupyter notebook notebooks/02_eda_analysis.ipynb
```

**What it does:**
- Creates 10 professional visualizations
- Analyzes demographics, financials, payment behavior
- Validates alternative data effectiveness (21% risk reduction)
- Statistical testing (Mann-Whitney U, correlation analysis)

**Output:** `visualizations/` folder with 10 PNG charts

#### Step 3: Feature Engineering (Coming in Review 2)
```bash
jupyter notebook notebooks/03_feature_engineering.ipynb
```

**What it will do:**
- Aggregate 6 supplementary tables into main dataset
- Create 150+ features (traditional + alternative + interaction)
- Handle missing values with MICE imputation
- Generate feature importance rankings

### Running Python Scripts
```python
# Load and preprocess data
from src.data_loader import load_all_data
from src.preprocessing import preprocess_pipeline

train, bureau, pos_cash, installments = load_all_data()
X_train, y_train = preprocess_pipeline(train)

# Train baseline model (upcoming)
from src.models import train_baseline_models

models = train_baseline_models(X_train, y_train)
```

---

## 🔬 Methodology

### 4-Phase Modeling Pipeline

#### Phase 1: Data Integration
```
Input: 7 separate tables
Process:
  ├─ Merge tables by SK_ID_CURR (customer ID)
  ├─ Aggregate supplementary data (sum, mean, count)
  ├─ Handle missing values (MICE imputation)
  └─ Scale numeric features (StandardScaler)
Output: Single feature matrix per application
```

#### Phase 2: Feature Engineering ⭐
```
Traditional Features (50):
  ├─ Demographics: Age groups, education encoding
  ├─ Financial: Income brackets, credit ratios, leverage
  └─ Employment: Tenure, industry risk factors

Alternative Features (50) - OUR INNOVATION:
  ├─ Payment Behavior: Regularity scores, early payment flags
  ├─ Bureau Network: Credit diversity, institution count
  ├─ Geographic Social: Region risk scores, community indicators
  └─ Temporal: Days since phone change, ID publish

Interaction Features (30):
  ├─ Age × Income
  ├─ Credit × Income  
  ├─ Region × Income
  └─ External source combinations

Total: ~150 features
```

#### Phase 3: Model Training
```
Review 2 - Baseline Models:
  ├─ Logistic Regression (interpretable baseline)
  ├─ Random Forest (non-linear patterns)
  └─ XGBoost (gradient boosting)
  Target: ROC-AUC > 0.75

Review 3 - Advanced Models:
  ├─ LightGBM (optimized for large data)
  ├─ CatBoost (handles categoricals natively)
  └─ Stacking Ensemble (combine predictions)
  Target: ROC-AUC > 0.80

Class Imbalance Handling:
  ├─ SMOTE (oversample minority class)
  ├─ Class weights in loss function
  └─ Stratified K-fold cross-validation
```

#### Phase 4: Evaluation & Deployment
```
Metrics:
  ├─ ROC-AUC (primary)
  ├─ Precision-Recall AUC
  ├─ F1 Score
  └─ Confusion Matrix

Explainability:
  ├─ SHAP values (feature importance)
  ├─ LIME (individual predictions)
  └─ Partial dependence plots

Deployment:
  └─ Streamlit web application
```

---

## 📈 Results

### Review 1 - Data Analysis Complete ✅

#### Deliverables Generated
- ✅ 10 professional visualizations
- ✅ 12 detailed analytical reports
- ✅ 2 comprehensive Jupyter notebooks
- ✅ Statistical validation of hypotheses

#### Key Metrics Discovered

| Metric | Value | Insight |
|--------|-------|---------|
| **Default Rate** | 8.07% | Manageable class imbalance (1:11 ratio) |
| **Alternative Data Impact** | **21% risk reduction** | Bureau data: 7.25% → 5.72% default |
| **Utility Proxy Validation** | **68.4% pay early** | Strong financial discipline signal |
| **Top Predictor** | EXT_SOURCE_3 (r=0.179) | Alternative scores > traditional metrics |
| **Target Segment** | 2,470 (0.8%) no data | Underbanked population to serve |
| **Missing Data** | 67/122 features | MICE imputation strategy required |

#### Correlation Analysis - Top Predictors
```
1. EXT_SOURCE_3             0.179  ⭐ Alternative credit score
2. EXT_SOURCE_2             0.160  ⭐ Alternative credit score  
3. EXT_SOURCE_1             0.155  ⭐ Alternative credit score
4. AGE_YEARS                0.078     Demographics
5. CREDIT_GOODS_RATIO       0.069     Financial
6. REGION_RATING            0.061     Geographic
7. DAYS_LAST_PHONE_CHANGE   0.055     Behavioral stability
```

**Insight:** Alternative data scores dominate top predictors - validates our approach!

### Review 2 - Model Training (In Progress)

**Target:** ROC-AUC > 0.75  
**Status:** Starting February 16, 2026  
**Expected Completion:** February 22, 2026  

### Review 3 - Advanced Models (Upcoming)

**Target:** ROC-AUC > 0.80  
**Status:** Planned for March 1, 2026  

### Review 4 - Deployment (Final)

**Target:** Production-ready web application  
**Status:** Planned for March 8, 2026  

---

## 🗓️ Roadmap

### 4-Week Development Timeline
```
Week 1 (Feb 11-14) ✅ COMPLETE
├─ Day 1: Data loading & exploration
├─ Day 2: EDA & visualizations  
├─ Day 3: Methodology design
├─ Day 4: Review 1 presentation
└─ Deliverable: 10 visualizations, 12 reports, validated approach

Week 2 (Feb 15-22) 🔄 IN PROGRESS
├─ Day 5-6: Preprocessing pipeline
├─ Day 7-8: Feature engineering (150 features)
├─ Day 9-10: Baseline model training
├─ Day 11: Review 2 preparation
└─ Deliverable: 3 baseline models, ROC-AUC > 0.75

Week 3 (Feb 23-Mar 1) 📅 UPCOMING
├─ Day 12-13: CFPB social data integration
├─ Day 14: Advanced model training (ensemble)
├─ Day 15: SHAP explainability
├─ Day 16-17: Streamlit web app prototype
├─ Day 18: Review 3 preparation
└─ Deliverable: Advanced model (ROC-AUC > 0.80), working demo

Week 4 (Mar 2-8) 🏁 FINAL
├─ Day 19-20: Cloud deployment (Streamlit Cloud)
├─ Day 21: Model monitoring dashboard
├─ Day 22: Business impact analysis
├─ Day 23-24: Final documentation
├─ Day 25: Final presentation preparation
└─ Deliverable: Production application, complete docs
```

### Feature Roadmap

- [x] Data exploration & profiling
- [x] EDA with 10 visualizations
- [x] Alternative data validation
- [ ] Preprocessing pipeline
- [ ] Feature engineering (150 features)
- [ ] Baseline model training
- [ ] CFPB social data integration
- [ ] Advanced model (ensemble)
- [ ] SHAP explainability
- [ ] Streamlit web application
- [ ] Cloud deployment
- [ ] Model monitoring

---

## 🛠️ Technologies Used

### Core Libraries

| Category | Technologies |
|----------|-------------|
| **Data Processing** | ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white) |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?logo=python&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?logo=python&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white) |
| **Machine Learning** | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white) ![XGBoost](https://img.shields.io/badge/XGBoost-EB5424?logo=xgboost&logoColor=white) ![LightGBM](https://img.shields.io/badge/LightGBM-02569B?logo=lightgbm&logoColor=white) |
| **Statistical Analysis** | ![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white) ![Statsmodels](https://img.shields.io/badge/Statsmodels-3776AB?logo=python&logoColor=white) |
| **Explainability** | SHAP, LIME |
| **Deployment** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) |
| **Development** | ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) |

### Requirements
```txt
# Core Data Science
pandas>=1.5.0
numpy>=1.23.0
scipy>=1.9.0

# Visualization
matplotlib>=3.6.0
seaborn>=0.12.0
plotly>=5.11.0

# Machine Learning
scikit-learn>=1.1.0
xgboost>=1.7.0
lightgbm>=3.3.0
catboost>=1.1.0

# Model Interpretation
shap>=0.41.0
lime>=0.2.0

# Missing Data Handling
scikit-learn>=1.1.0  # For MICE/IterativeImputer

# Utilities
tqdm>=4.64.0
joblib>=1.2.0

# Deployment
streamlit>=1.15.0

# Notebook
jupyter>=1.0.0
ipykernel>=6.17.0
```

---

## 👥 Team

### TECH CRUSADERS

<table>
<tr>
<td align="center">
<img src="https://github.com/Nithilan77.png" width="100px;" alt=""/><br />
<sub><b>Nithilan S</b></sub><br/>
<a href="https://github.com/Nithilan77">GitHub</a>
</td>
<td align="center">
<sub><b>Muskan Kumari V</b></sub><br/>
Team Member
</td>
<td align="center">
<sub><b>Charumadhi M</b></sub><br/>
Team Member
</td>
</tr>
</table>

**Department:** Information Technology  
**Institution:** [Your Institution Name]  
**Hackathon:** Zenith Hackathon 5.0  
**Date:** February 2026  

---

## 🙏 Acknowledgments

- **Zenith Hackathon 5.0** for organizing this challenge
- **Home Credit** for providing the comprehensive alternative lending dataset
- **Kaggle** for hosting the data and enabling data science competitions
- **Open Source Community** for the amazing ML libraries (scikit-learn, XGBoost, pandas)
- Our mentors and reviewers for valuable feedback

### Inspiration & References

- [Home Credit Default Risk Competition](https://www.kaggle.com/c/home-credit-default-risk)
- ["Alternative Data in Credit Scoring"](https://www.bis.org/publ/work834.pdf) - BIS Working Paper
- [SHAP Documentation](https://shap.readthedocs.io/)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
MIT License

Copyright (c) 2026 TECH CRUSADERS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📧 Contact

**Project Repository:** [https://github.com/Nithilan77/AltScore](https://github.com/Nithilan77/AltScore)

**Team Lead:** Nithilan S - [@Nithilan77](https://github.com/Nithilan77)

**Questions?** Open an [issue](https://github.com/Nithilan77/AltScore/issues) or contact us directly!

---

## 🌟 Star History

If you found this project helpful, please consider giving it a ⭐!

[![Star History Chart](https://api.star-history.com/svg?repos=Nithilan77/AltScore&type=Date)](https://star-history.com/#Nithilan77/AltScore&Date)

---

<div align="center">

**Made with ❤️ by TECH CRUSADERS**

*Building fair credit access for everyone, one algorithm at a time.*

[⬆ Back to Top](#altscore---alternative-credit-scoring-system-)

</div>


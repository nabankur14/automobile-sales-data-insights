# 🚗 Automobile Sales Data Insights

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Optimizing Marketing Campaigns & Customer Experience for Austo Motor Company**

---

## 📖 Table of Contents
- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Dataset](#-dataset)
- [Methodology](#-methodology)
- [Key Results](#-key-results)
- [Business Impact](#-business-impact)
- [Tech Stack](#-tech-stack)
- [Repository Structure](#-repository-structure)
- [How to Run](#-how-to-run)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 🔭 Project Overview
**Austo Motor Company**, a leading manufacturer of SUVs, Sedans, and Hatchbacks, is looking to enhance its marketing efficiency. This project analyzes customer data to understand demand patterns, refine customer segmentation, and provide data-driven recommendations to improve campaign performance and customer experience.

## 💼 Business Problem
The board of Austo Motor Company raised concerns about the **efficiency of the current marketing campaign**. The key objectives are:
- 📉 Reduce marketing waste by targeting the right audience.
- 🎯 Identify high-value customer segments.
- 🚗 Understand product preferences (SUV vs. Sedan vs. Hatchback) based on demographics.
- 💡 Provide actionable insights to improve sales and customer retention.

## 📊 Dataset
The dataset contains customer demographic and financial details.
- **Source:** Internal Company Data (Austo Motor Company)
- **Size:** ~1,600 Records
- **Key Features:**
  - `Age`, `Gender`, `Marital Status`, `Profession`, `Education`
  - `Salary`, `Partner Salary`, `Total Salary`
  - `No. of Dependents`, `Partner Working`
  - `Personal Loan`, `House Loan` (Financial Liabilities)
  - `Price`, `Make` (Target Variables)

## ⚙️ Methodology
1. **Data Cleaning:** Handling missing values, correcting data types, and removing duplicates (e.g., standardizing 'Femal'/'Femle' to 'Female').
2. **Exploratory Data Analysis (EDA):** Univariate and Bivariate analysis to uncover patterns in age, salary, and car preferences.
3. **Feature Engineering:** Creating new features like `Total_Salary` to better assess purchasing power.
4. **Customer Profiling:** Segmenting customers based on profession, family size, and income to map them to specific car types.
5. **Insights Generation:** Deriving business-centric conclusions from the data patterns.

## 📈 Key Results
- **Income Influence:** Higher `Total_Salary` strongly correlates with purchasing **SUVs**, while entry-level buyers prefer **Hatchbacks**.
- **Demographics:** 
  - **Sedans** are popular among middle-aged, salaried professionals.
  - **SUVs** are preferred by customers with larger families and higher disposable income.
- **Gender Trends:** Distinct preferences were observed, with significant insights into female buyers' growing market share in specific segments.

## 🚀 Business Impact
1. **Targeted Marketing:** Shift ad spend for SUVs towards high-income, married professionals with dependents.
2. **Product Positioning:** Position Hatchbacks as the ideal "first car" for young, single professionals or students.
3. **Loan Offers:** Partner with banks to offer tailored financing for customers with existing liabilities (House/Personal loans), as they show high intent but price sensitivity.

## 💻 Tech Stack
- **Language:** Python
- **Libraries:**
  - 🐼 `Pandas`, `NumPy` (Data Manipulation)
  - 📊 `Matplotlib`, `Seaborn` (Visualization)
  - 📉 `SciPy` (Statistical Analysis)
- **Environment:** Jupyter Notebook

## 📂 Repository Structure
```
project-name/
│
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned data (if any)
│
├── notebooks/
│   └── analysis.ipynb        # Main analysis notebook
│
├── src/                      # Source code for reproduction
│   ├── data_preprocessing.py
│   ├── modeling.py
│   └── evaluation.py
│
├── reports/
│   └── business_report.pdf   # Detailed business report
│
├── visuals/                  # Exported charts and plots
│   └── charts/
│
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🏃 How to Run
1. **Clone the repository:**
   ```bash
   git clone https://github.com/nabankur14/automobile-sales-data-insights.git
   cd automobile-sales-data-insights
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Notebook:**
   ```bash
   jupyter notebook notebooks/analysis.ipynb
   ```

## 🛠 Future Improvements
- [ ] **Predictive Modeling:** Build a classification model to predict which car type a new customer is likely to buy.
- [ ] **Dashboarding:** Create an interactive Tableau or PowerBI dashboard for the marketing team.
- [ ] **External Data:** Integrate macroeconomic data to see how inflation impacts car sales.

## 👨‍💻 Author
**Nabankur Ray**  
*Data Science Student*  
[GitHub Profile](https://github.com/nabankur14) | [LinkedIn](https://linkedin.com/in/nabankur-ray)

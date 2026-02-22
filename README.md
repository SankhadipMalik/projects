# 📊 Bank Marketing EDA Project

## 📌 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on the Bank Marketing Dataset.  
The goal is to analyze customer data and identify patterns that influence term deposit subscription.

---

## 📂 Dataset Information

The dataset contains customer details such as:

- Age
- Job
- Marital Status
- Education
- Balance
- Housing Loan
- Personal Loan
- Contact Type
- Campaign Details
- Call Duration
- Deposit Subscription (Target Variable)

---

## 🛠️ Technologies Used

- Python 🐍
- Pandas
- Seaborn
- Matplotlib

---

## 🔎 Steps Performed

### 1️⃣ Data Loading
- Loaded CSV dataset using Pandas

### 2️⃣ Data Cleaning
- Checked missing values
- Removed duplicates
- Standardized column names

### 3️⃣ Outlier Detection
- Used IQR method on `age`
- Removed extreme values

### 4️⃣ Data Visualization
- Age Distribution Histogram
- Job Distribution
- Marital Status Distribution
- Deposit Subscription Count
- Call Duration vs Deposit (Boxplot)

---

## 📊 Key Insights

- Call duration significantly impacts deposit subscription.
- Certain job categories show higher subscription rates.
- Age distribution mostly falls within working-class range.

---

## 📁 Project Structure

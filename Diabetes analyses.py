import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Load the dataset
df = pd.read_csv(r"C:\Users\91983\Downloads\diabetes.csv")
#column names
df.columns = df.columns.str.strip().str.lower()
print("Columns:\n", df.columns)
# basic info
print(df.head())
print(df.info())
print(df.describe())
# Check for missing values
print("missing values:\n", df.isnull().sum())

# as in diabetes 0 means no diabetes and 1 means diabetes, we can check the distribution of the target variable

cols_with_zero = ['glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi']
df[cols_with_zero] = df[cols_with_zero].replace(0, np.nan)
print("\n after handling missing values:\n" , df.isnull().sum())

#outlier detection
plt.figure(figsize=(8,6))
sns.boxplot(data=df[['glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi']])
plt.title("Boxplot of Features with Zero Values")
plt.show()

 #VISUALIZATION

# Age distribution
sns.histplot(df["age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

# Glucose vs Outcome
sns.boxplot(x="outcome", y="glucose", data=df)
plt.title("Glucose vs Diabetes")
plt.show()

# BMI vs Outcome
sns.boxplot(x="outcome", y="bmi", data=df)
plt.title("BMI vs Diabetes")
plt.show()

# Outcome count
sns.countplot(x="outcome", data=df)
plt.title("Diabetes Outcome Count")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
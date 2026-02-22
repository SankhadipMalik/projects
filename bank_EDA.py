import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 1️⃣ LOAD DATASET (COMMA CSV)
df = pd.read_csv("bank.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

print("Columns:\n", df.columns)


# 2️⃣ BASIC INFO

print(df.head())
print(df.info())
print(df.describe())
print(df.describe(include="object"))


# 3️⃣ MISSING VALUES

print(df.isnull().sum())


# 4️⃣ OUTLIER DETECTION

plt.figure(figsize=(8,6))
sns.boxplot(x=df["age"])
plt.show()

q1 = df["age"].quantile(0.25)
q3 = df["age"].quantile(0.75)
iqr = q3 - q1

df = df[
    (df["age"] >= q1 - 1.5 * iqr) &
    (df["age"] <= q3 + 1.5 * iqr)
]

print("Shape after outlier removal:", df.shape)


# 5️⃣ CLEANING

df.drop_duplicates(inplace=True)


# 6️⃣ VISUALIZATION

sns.histplot(df["age"], bins=30, kde=True)
plt.show()

sns.countplot(x="job", data=df)
plt.xticks(rotation=90)
plt.show()

sns.countplot(x="marital", data=df)
plt.show()

sns.countplot(x="deposit", data=df)
plt.show()


# 7️⃣ CAMPAIGN ANALYSIS

plt.figure(figsize=(8,6))
sns.boxplot(x="deposit", y="duration", data=df)
plt.show()
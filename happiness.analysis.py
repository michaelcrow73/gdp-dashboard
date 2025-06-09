import pandas as pd

# Load the dataset
df = pd.read_csv('data/happiness_2017.csv')

# Preview the first 5 rows
print("🔍 First 5 rows:")
print(df.head())

# Basic info about the dataset
print("\n🧾 Dataset Info:")
print(df.info())

# Summary statistics
print("\n📊 Summary Statistics:")
print(df.describe())

# Check for missing values
print("\n🧼 Missing Values:")
print(df.isnull().sum())

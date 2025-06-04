import pandas as pd

pd.set_option('display.max_colwidth', None)

csv_path = r'D:\Diploma\data\MC-EIU-processed_local.csv'
df = pd.read_csv(csv_path)

print("\nFirst 15 rows of the dataset:")
df.head(15)

print("\n=== DataFrame Info ===")
df.info()

print("\n=== Basic Statistics ===")
df.describe(include='all')

print("\n=== Missing Values per Column ===")
df.isnull().sum()

print("\n=== Unique Values per Column ===")
df.nunique()

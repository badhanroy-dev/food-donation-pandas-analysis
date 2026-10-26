import pandas as pd
df = pd.read_csv("food_donations.csv",sep="\t")
df["Quantity_kg"] = df["Quantity_kg"].replace("Missing",pd.NA)
df["Quantity_kg"] = pd.to_numeric(df["Quantity_kg"])
# print(df)
# print(df.head()) #returns the first five rows by default
# print(df.tail(3)) # returns the last 3 rows
# print(df.shape)
# print(df.columns)
# print(df.dtype) # shows data types of each column
# print(df.isnull().sum())
print(df.describe())


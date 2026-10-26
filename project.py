import pandas as pd
df = pd.read_csv("food_donations.csv",sep="\t")
df["Quantity_kg"] = df["Quantity_kg"].replace("Missing",pd.NA)
df["Quantity_kg"] = pd.to_numeric(df["Quantity_kg"])
#loading and inspecting data
# print(df)
# print(df.head()) #returns the first five rows by default
# print(df.tail(3)) # returns the last 3 rows
# print(df.shape)
# print(df.columns)
# print(df.dtype) # shows data types of each column
# print(df.isnull().sum())
# print(df.describe())
#Selecting and filtering data
# print(df[["Donor","Quantity_kg"]])
# print(df["Food_Type"])
# print(df.iloc[0:3])
# print(df[df["Donation_ID"] == 3])
# print(df[df["Status"]=="Available"])
# print(df[df["Quantity_kg"] > 20])
# print(df[(df["Status"]=="Available") & (df["Quantity_kg"] > 15)])
# print(df[df["City"].isin(["Dhaka","Gazipur"])]) # donations belonging to either Dhaka or Gazipur
# print(df[df["Quantity_kg"].between([15,30])]) # donations whose quantity is between 15 kg and 30 kg (inclusive)
#Cleaning data
# print(df.duplicated().sum())
# df = df.drop_duplicates()
# print(df.shape)
mean_quantity =  df["Quantity_kg"].mean()
df["Quantity_kg"] = df["Quantity_kg"].fillna(mean_quantity)
# print(df["Quantity_kg"])
print(df.isnull().sum())
df = df.reset_index(drop=True)
print(df)




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
# print(df.isnull().sum())
# df = df.reset_index(drop=True)
# print(df)
#Creating and modifying Columns
# df.loc[df["Quantity_kg"] >=25, "Quantity_Status"] = "Large"
# df.loc[df["Quantity_kg"]<25, "Quantity_Status"] = "Small"
# print(df[["Quantity_kg","Quantity_Status"]])
# df["Donation_Value"] = df["Quantity_kg"] * 50
# print(df[["Quantity_kg","Donation_Value"]])
# df = df.drop(columns=["Donation_Value"])
# print(df.columns)
#Sorting and Counting
df = df.sort_values(by="Quantity_kg",ascending=False)
print(df.head(5))
print(df["Food_Type"].value_counts())
print(df["Status"].value_counts())
print(df["Donor"].nunique()) #finds the number of unique donors





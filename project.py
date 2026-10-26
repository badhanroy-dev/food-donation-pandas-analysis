import pandas as pd
df = pd.read_csv("food_donations.csv",sep="\t")
df["Quantity_kg"] = df["Quantity_kg"].replace("Missing",pd.NA)
df["Quantity_kg"] = pd.to_numeric(df["Quantity_kg"])
#loading and inspecting data
print(df)
print("Dsiplay the first five rows")
print(df.head()) #returns the first five rows by default
print("Dsiplay the last three rows")
print(df.tail(3)) # returns the last 3 rows
print("Display the number of rows and columns")
print(df.shape)
print(df.columns)
print(df.dtypes) # shows data types of each column
print("Number of missing values in each column")
print(df.isnull().sum())
print("displaying statistics")
print(df.describe())
# Selecting and filtering data
print(df[["Donor","Quantity_kg"]])
print(df["Food_Type"])
print(df.iloc[0:3])
print("record with Donation_ID equal to 3")
print(df[df["Donation_ID"] == 3])
print("all donations whose status is Available")
print(df[df["Status"]=="Available"])
print("donations with a quantity greater than 20 kg")
print(df[df["Quantity_kg"] > 20])
print("donations that are both Available and greater than 15 kg")
print(df[(df["Status"]=="Available") & (df["Quantity_kg"] > 15)])
print("donations belonging to either Dhaka or Gazipur")
print(df[df["City"].isin(["Dhaka","Gazipur"])]) # donations belonging to either Dhaka or Gazipur
print("donations whose quantity is between 15 kg and 30 kg")
print(df[df["Quantity_kg"].between(15,30)]) # donations whose quantity is between 15 kg and 30 kg (inclusive)
# Cleaning data
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df.shape)
mean_quantity =  df["Quantity_kg"].mean()
df["Quantity_kg"] = df["Quantity_kg"].fillna(mean_quantity)
print(df["Quantity_kg"])
print(df.isnull().sum())
df = df.reset_index(drop=True)
print(df)
#Creating and modifying Columns
df.loc[df["Quantity_kg"] >=25, "Quantity_Status"] = "Large"
df.loc[df["Quantity_kg"]<25, "Quantity_Status"] = "Small"
print(df[["Quantity_kg","Quantity_Status"]])
df["Donation_Value"] = df["Quantity_kg"] * 50
print(df[["Quantity_kg","Donation_Value"]])
df = df.drop(columns=["Donation_Value"])
print(df.columns)
#Sorting and Counting
df = df.sort_values(by="Quantity_kg",ascending=False)
print(df.head(5))
print(df["Food_Type"].value_counts())
print(df["Status"].value_counts())
print(df["Donor"].nunique()) #finds the number of unique donors
#Grouping and statistics
print("total quantity of food donated")
print(df["Quantity_kg"].sum())
print("largest donation quantities")
print(df["Quantity_kg"].max())
print("Smallest donation quantities")
print(df["Quantity_kg"].min())
print("Total Quantity donated by each donor")
print(df.groupby("Donor")["Quantity_kg"].sum())
print("Total Quantity for each food type")
print(df.groupby("Food_Type")["Quantity_kg"].sum())
print("Number of donations in each city")
print(df.groupby("City")["Donation_ID"].count())
print("total quantity of food currently available")
available = df[df["Status"] == "Available"]
print(available["Quantity_kg"].sum())
print("total quantity of food claimed")
available = df[df["Status"] == "Claimed"]
print(available["Quantity_kg"].sum())
#Exporting results
df.to_csv("cleaned_food_donations.csv",index=False)
food_summary = df.groupby("Food_Type")["Quantity_kg"].sum()
food_summary = food_summary.reset_index() # reset_index() converts the grouped result into a regular DataFrame with Food_Type as a column
food_summary.to_csv("food_summary.csv",index=False)
print(food_summary)




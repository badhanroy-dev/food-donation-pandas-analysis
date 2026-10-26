# Food Donation Pandas Analysis

My first Pandas practice project, created to learn and apply fundamental Pandas syntax through a simple food donation dataset.

## About the Project

This project analyzes food donation records to understand donation quantities, food categories, donor contributions, and donation statuses. It focuses on practicing basic data manipulation and analysis using Python's Pandas library.

## Technologies Used

- Python
- Pandas
- CSV files

## Dataset

The dataset contains food donation records with the following information:

- Donation ID
- Donor name
- Food type
- Quantity in kilograms
- Donation status
- City

The dataset includes a missing value and a duplicate record for practicing data cleaning.

## Concepts Practiced

- Loading and inspecting CSV files
- Selecting columns and filtering rows
- Handling missing values and duplicate records
- Creating, modifying, and removing columns
- Sorting and counting values
- Calculating basic statistics
- Grouping data using `groupby()`
- Exporting results to CSV files

## Project Files

- `food_donations.csv` — Original dataset
- `food_donation_analysis.ipynb` — Notebook containing the code, explanations, and outputs
- `cleaned_food_donations.csv` — Cleaned dataset
- `food_summary.csv` — Summary of total donation quantities by food type

## How to Run

1. Clone or download this repository.
2. Install the required library:

   ```bash
   pip install pandas
   ```

3. Open `project.py` in VS Code.
4. Run the file.

The notebook uses the original CSV file to perform the analysis and generate the output CSV files.

## Purpose

This project is part of my learning journey in data analysis. My goal was to become familiar with Pandas syntax and understand its basic operations through hands-on practice.

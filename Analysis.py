import pandas as pd

# Read the Excel file (replace the filename with your actual path)
df = pd.read_excel("raw_customer_reviews_extended.xlsx")

# Separate the 'Customer_Review_Text' column into parts
split_cols = df["Customer_Review_Text"].str.extract(r"^(\d+)\s+(.*?)\s*\|\s*(\d)\s*\|\s*(\w+)\s*\|\s*(\w+)$")

# Rename the columns
split_cols.columns = ["Review ID", "Review Text", "Rating", "Category", "Price Level"]

# Display the final clean DataFrame
print(split_cols.head())

# Optional: save to new clean Excel file
split_cols.to_excel("clean_customer_reviews.xlsx", index=False)
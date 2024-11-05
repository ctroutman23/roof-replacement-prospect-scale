# Import packages
import pandas as pd

# Read in real estate data
real_estate_df = pd.read_csv("data/realtor-data.zip.csv")

# Take a look at real estate data - It may be best to run one line at a time
# print(real_estate_df.describe())
# print(real_estate_df.head())
# print(real_estate_df.columns)

# Clean real estate data

#Select the rows for the state you want to sell roofs in, personally I'm in KY
real_estate_df = real_estate_df[real_estate_df["state"] == "Kentucky"]

# Take a look at the filtered dataset to make sure it worked
# print(real_estate_df.head())

# Get the number of rows you're working with
print(len(real_estate_df)) #Kentucky rows = 26,316
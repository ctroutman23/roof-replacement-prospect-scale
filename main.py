# Import packages
import pandas as pd

# Read in real estate data
real_estate_df = pd.read_csv("data/marketing_sample_for_trulia_com-trulia_property_data__20200101_20200131__5k_data.csv")


# Clean real estate data

  # Replace white space in column names with underscores
real_estate_df.columns = real_estate_df.columns.str.replace(' ', '_')
# print(real_estate_df.columns.tolist())    Check to see if it worked

  # Filter dataframe down to relevant columns
relevant_columns = ['Uniq_Id', 'Address_Full', 'Price', 'Sqr_Ft', 'Year_Built', 'Price_Sqr_Ft',
                    'Last_Sold_Year']
real_estate_df = real_estate_df[relevant_columns]
print(real_estate_df)


# Write code to generate roofing lead rating (scale of 1-5)

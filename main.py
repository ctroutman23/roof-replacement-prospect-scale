# Import packages
import pandas as pd
import re

# Read in real estate data
real_estate_df = pd.read_csv('data/marketing_sample_for_trulia_com-trulia_property_data__20200101_20200131__5k_data.csv')


# Clean real estate data

  # Replace white space in column names with underscores
real_estate_df.columns = real_estate_df.columns.str.replace(' ', '_')

  # Filter dataframe down to relevant columns
relevant_columns = ['Uniq_Id', 'Address_Full', 'Price', 'Sqr_Ft', 'Price_Sqr_Ft',
                    'Year_Built', 'Last_Sold_Year', 'Features', 'Description']
real_estate_df = real_estate_df[relevant_columns]

  # Filter dataframe to only include homes built in the last 20-30 years
real_estate_df = real_estate_df.loc[(real_estate_df.Year_Built >= 1994) & 
(real_estate_df.Year_Built <= 2004)]

  # Clean the Sqr_Ft column
real_estate_df['Sqr_Ft'] = real_estate_df['Sqr_Ft'].str.replace(',', '') #remove comma
real_estate_df['Sqr_Ft'] = real_estate_df['Sqr_Ft'].str.replace('sqft', '') #remove unit
real_estate_df['Sqr_Ft'] = pd.to_numeric(real_estate_df['Sqr_Ft'], errors='coerce') #convert missing values to NaN
real_estate_df = real_estate_df.dropna(subset=['Sqr_Ft']) #remove NaN values
real_estate_df['Sqr_Ft'] = real_estate_df['Sqr_Ft'].astype(int) #change data type to int

  # Sort/rank dataframe by Sqr-Ft in descending order
real_estate_df = real_estate_df.sort_values(by=['Sqr_Ft'], ascending=False)
print(real_estate_df.Sqr_Ft)

  # Extract relevant data from "Features" column




# Write code to generate roof replacement prospect score
# The best prospects are the mostt likely to need a new roof and the most expensive roof 
# replacement projects.



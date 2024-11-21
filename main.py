# Import packages
import pandas as pd
import re

# Read in real estate dataset #1
real_estate_df = pd.read_csv('data/marketing_sample_for_trulia_com-trulia_property_data__20200101_20200131__5k_data.csv')

# Read in real estate dataset #2
real_estate_df_2 = pd.read_csv('data/marketing_sample_for_trulia_com-real_estate__20190901_20191031__30k_data.csv')

# Clean real estate data

  # Replace white space in column names with underscores
real_estate_df.columns = real_estate_df.columns.str.replace(' ', '_')

real_estate_df_2.columns = real_estate_df_2.columns.str.replace(' ', '_')

  # Filter dataframe down to relevant columns
relevant_columns = ['Uniq_Id', 'Address_Full', 'Price', 'Sqr_Ft', 'Price_Sqr_Ft',
                    'Year_Built', 'Last_Sold_Year', 'Features', 'Description']
real_estate_df = real_estate_df[relevant_columns]
real_estate_df_2 = real_estate_df_2[relevant_columns]

  # After both datasets are given the same columns, combine the 2 datasets into 1
combined_real_estate_df = pd.concat([real_estate_df, real_estate_df_2])

  # Filter dataframe to only include homes built in the last 20-30 years
combined_real_estate_df = combined_real_estate_df.loc[(combined_real_estate_df.Year_Built >= 1994) & 
(combined_real_estate_df.Year_Built <= 2004)]

  # Clean the Sqr_Ft column
combined_real_estate_df['Sqr_Ft'] = combined_real_estate_df['Sqr_Ft'].str.replace(',', '') #remove comma
combined_real_estate_df['Sqr_Ft'] = combined_real_estate_df['Sqr_Ft'].str.replace('sqft', '') #remove unit
combined_real_estate_df['Sqr_Ft'] = combined_real_estate_df['Sqr_Ft'].apply(
  lambda x: int(x) if pd.notnull(x) else x) #change data type to int, leace NaN values alone

  #Cleam Price column
combined_real_estate_df['Price'] =  combined_real_estate_df['Price'].str.replace(',', '') #remove comma
combined_real_estate_df['Price'] = combined_real_estate_df['Price'].str.replace('$', '') #remove $
combined_real_estate_df['Price'] = pd.to_numeric(combined_real_estate_df['Price'], errors='coerce') #convert column values to numerical, handling non-convertablem values

  # Extract relevant roofing data from "Features" column
combined_real_estate_df['Features'] = combined_real_estate_df['Features'].str.split('|') #split each row in the features column on '|'

combined_real_estate_df['Features'] = combined_real_estate_df['Features'].apply(
  lambda features: next((item.strip() for item in features if 'roof:' in item.lower()), None)) #use anonymous func. to transform features column to only include roof info


combined_real_estate_df.rename(columns={'Features': 'Roof_Type'}, inplace=True) #Change the name of the features column to represent the new content                     
  

  #Save modified dataframe to csv
combined_real_estate_df.to_csv('cleaned_combined_data/real_estate_data.csv', index=False) 


# Write code to generate roof replacement prospect score
# The best prospects are the mostt likely to need a new roof and the most expensive roof 
# replacement projects.

#Our propsect score is based on 5 datapoints within our modified dataset:
#1. Price - drawn from latest recorded listing price
#2. Size - drawn from listed square footage of the home
#3. Age - drawn from the date the home was built
#4. Recent transactions - drawn from date of last sale
#5. Existing roof type - drawn from listing of roof material

#How the point scale works: 



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

  # Filter dataframe to only include homes built in the last 20-30 years (ideal timefram for homes needing a new roof)
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

#Our propsect score is based on 5 datapoints within our combined & modified dataset:

#1. Price - drawn from latest recorded listing price
# Initialize new column to hold price score
combined_real_estate_df['Price_Score'] = 0

# Assign points to the price points column based on the criteria below:
# 1 point given per $100,000k
combined_real_estate_df['Price_Score'] = (combined_real_estate_df['Price'] // 100000) * 1
# print(combined_real_estate_df['Price_Points'])


#2. Size - drawn from listed square footage of the home
# Initialize new column to hold size score
combined_real_estate_df['Size_Score'] = 0

# Assign points to the size points column based on the criteria below:
# 1 point given per 500 sq ft
combined_real_estate_df['Size_Score'] = (combined_real_estate_df['Sqr_Ft'] // 500) * 1
# print(combined_real_estate_df['Size_Points'])


#3. Age - drawn from the date the home was built
########## Think about changing the data and calculations to include homes odler than 30 years
# Initialize new column to hold age score
combined_real_estate_df['Age_Score'] = 0

# Assign points to the age points column based on the criteria below:
# 20-24 years = 5 points, 25-30 years = 10 points
# Write function to calculate score and apply to age score column
def calc_age_points(year_built):
  score = 0
  if 2000 <= year_built <= 2004:
    score += 5
  elif 1994 <= year_built <= 1999:
    score += 10
  return score
 
combined_real_estate_df['Age_Score'] = combined_real_estate_df['Year_Built'].apply(calc_age_points)
# print(combined_real_estate_df['Age_Score'])


#4. Recent Sales - drawn from date of last sale
# It's important to keep track of this because roofs often 
# get replaced during or soon after the home sale process.
# Initialize new column to hold the recent sale score
combined_real_estate_df['Recent_Sale_Score'] = 0

# Assign points to the recent sale score column based on the criteria below:
#   -Homes sold this year lose 10 points
#   -Homes sold within the last 1-5 years lose 8 points
#   -Homes sold within the last 6-10 years lose 4 points
#   -Homes sold within the last 11-15 years lose 0 points
#   -Homes sold within the last 16-20 years gain 4 points
#   -Homes sold within the last 21-25 years gain 8 points
#   -Homes sold within the last 26-30 years gain 10 points
#   -If the last date sold is not listed, then no points are taken away or added.
# Create function to calculate the recent sale score
def calc_recent_sale_score(Last_Sold_Year):
  score = 0
  if Last_Sold_Year == 2024:
    score -= 10
  elif  2019 <= Last_Sold_Year <= 2023:
    score -= 8
  elif 2014 <= Last_Sold_Year <= 2018:
    score -= 4
  elif 2009 <= Last_Sold_Year <= 2013: #I know this isn't necessary, I'm just practicing
    score = 0
  elif 2004 <= Last_Sold_Year <= 2008:
    score += 4
  elif 1999 <= Last_Sold_Year <= 2003:
    score += 8
  elif 1994 <= Last_Sold_Year <= 1998:
    score += 10
  return score

# Apply function to 'Last_Sold_Year' column
combined_real_estate_df['Recent_Sale_Score'] = combined_real_estate_df['Last_Sold_Year'].apply(
  calc_recent_sale_score
)
# print(combined_real_estate_df['Recent_Sale_Score'])


#5. Existing roof type - drawn from listing of roof material
"""
For our company at least, we mainly replace roofs with asphalt. This is because 
asphalt roofs are the roofs that also need to be replaced the most. We install quality
asphalt roof systems, but they just don't last as long as more expensive systems like metal
and slate. 

With this real estate data, we are able to see the type of roof on many of these homes.
We can deduce that a home with an asphalt roof is likely a better prospect for a roof 
replacement. We can even use the data to compare the type of roof with the age of the home 
and make deductions about the propsect of replacing that roof based on the expected life 
of its declared roof system.
"""
# For now, we'll just initialize a points column that weighs the score in favor of homes
# with asphalt roofs.

# Initialize new column to hold the roof type score
combined_real_estate_df['Roof_Type_Score'] = 0

# Write function to check for specific roof types in our dataset
def find_roof_type(roof_type):
  if combined_real_estate_df['Roof_Type'].str.contains(roof_type, case=False).any():
    print("This exists in the Roof_Type column.")
  else:
    print("This does not exist in the Roof_Type column.")

# print(combined_real_estate_df['Roof_Type'])
# asphalt = find_roof_type('asphalt') #Yes

# metal = find_roof_type('metal') #Yes

# slate = find_roof_type('slate') #Yes

# tile = find_roof_type('tile') #Yes

# wood = find_roof_type('wood') #No

# shake = find_roof_type('shake') #Yes

# composition = find_roof_type('composition') #Yes

# laminate = find_roof_type('laminate') #No

# Write a function to calculate the roof type score based on the criteria below:
#   -Homes with asphalt or composition roofs gain 50 points
#   -Homes with metal roofs lose 30 points
#   -Homes with slate or tile roofs lose 40 points
#   -Homes with shake (wooden) roofs lose 50 points
#   -Homes with no stated roof type are unaffected 

def calc_roof_type_score(roof_type):
    score = 0
    if roof_type is None:
        return score  # Handle None or NaN
    roof_type = roof_type.lower()  # Make case insensitive
    if 'asphalt' in roof_type or 'composition' in roof_type:
        score += 50
    elif 'metal' in roof_type:
        score -= 30
    elif 'slate' in roof_type or 'tile' in roof_type:
        score -= 40
    elif 'shake' in roof_type:
        score -= 50
    return score

# Apply function to 'Roof_Type' column
combined_real_estate_df['Roof_Type_Score'] = combined_real_estate_df['Roof_Type'].apply(
  calc_roof_type_score
)
# print(combined_real_estate_df['Roof_Type_Score'])


# Create the final propsect score column based on the scores in the 5 new columns created
# from our dataset.
combined_real_estate_df['Final_Prospect_Score'] = combined_real_estate_df['Price_Score'] + combined_real_estate_df['Size_Score'] + combined_real_estate_df['Age_Score'] + combined_real_estate_df['Recent_Sale_Score'] + combined_real_estate_df['Roof_Type_Score']
print(combined_real_estate_df['Final_Prospect_Score'])

#How the point scale works: 
#The scale is currently heavily weighted toward the biggest most expensive homes



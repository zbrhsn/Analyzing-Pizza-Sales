#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: Zubayer
"""

import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Excel files

pizza_sales_df = pd.read_excel('pizza_sales.xlsx')
pizza_size_df = pd.read_csv('pizza_size.csv')
pizza_category_df = pd.read_csv('pizza_category.csv')

# Viewing top and bottom rows in a DataFrame
pizza_sales_df.head()
pizza_sales_df.head(10)

pizza_sales_df.tail()
pizza_sales_df.tail(10)

# Describing the data
pizza_sales_df.describe()
pizza_description = pizza_sales_df.describe()

# Have a look at non-null counts per column
pizza_sales_df.info()

# Count the number of null values in each column
null_count = pizza_sales_df.isnull().sum()

# Check for duplicated rows
duplicated_rows = pizza_sales_df.duplicated().sum()
print(duplicated_rows)

# To select a column

quantity_column = pizza_sales_df['quantity']
selected_columns = pizza_sales_df[['order_id', 'quantity', 'unit_price']]

# Get the row with index label 3
row = pizza_sales_df.loc[3]

# Get two rows, index label 3 and 5
rows = pizza_sales_df.loc[[3, 5]]

# Get rows between index labels 3 and 5
subset = pizza_sales_df.loc[3:5]

# Get rows between index labels 3 and 5 and specific columns
subset = pizza_sales_df.loc[3:5, ['quantity', 'unit_price']]

# Set an index as a column in a DataFrame
pizza_sales_df.set_index('order_details_id', inplace=True)

# Resetting an index
pizza_sales_df.reset_index(inplace = True)

# Truncate DataFrame before index 3
truncated_before = pizza_sales_df.truncate(before=3)

# Truncate DataFrame after index 5
truncated_after = pizza_sales_df.truncate(after=5)

# Truncating columns
quantity_series = pizza_sales_df['quantity']

# Truncate series before index 3
truncated_series_before = quantity_series.truncate(before=3)

# Truncate series after index 5
truncated_series_after = quantity_series.truncate(after=5)

# Basic Filtering
filtered_rows = pizza_sales_df[pizza_sales_df['unit_price'] > 20]

# Filtering on date
pizza_sales_df['order_date'] = pizza_sales_df['order_date'].dt.date
date_target = datetime.strptime('2015-12-15', '%Y-%m-%d').date()
filtered_rows_by_date = pizza_sales_df[pizza_sales_df['order_date'] > date_target]

# Filtering on Multiple Conditions
# Using the and condition
bbq_chicken_rows = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) 
                                  & (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]

# Using the or condition |
bbq_chicken_rows_or = pizza_sales_df[(pizza_sales_df['unit_price'] > 20) 
                                  | (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]


# Filter a specific range
high_sales = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) & (pizza_sales_df['unit_price'] <= 20)]

# Dropping null values
pizza_sales_null_values_dropped = pizza_sales_df.dropna()
null_count = pizza_sales_null_values_dropped.isnull().sum()

# Replace nulls with a value
date_na_fill = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
pizza_sales_null_replaced = pizza_sales_df.fillna(date_na_fill)

# Deleting specific rows and columns in a DataFrame
filtered_rows_2 = pizza_sales_df.drop(2, axis=0)

# Deleting rows 5,7,9
filtered_rows_5_7_9 = pizza_sales_df.drop([5,7,9], axis=0)

# Delete a column by column name
filtered_unit_price = pizza_sales_df.drop('unit_price', axis=1)

# Delete multiple columns
filtered_unit_price_and_order_id = pizza_sales_df.drop(['unit_price', 'order_id'], axis=1)

# Sorting a DataFrame in Pandas

# Sorting in ascending order
sorted_df = pizza_sales_df.sort_values('total_price')

# Sorting in descending order
sorted_df = pizza_sales_df.sort_values('total_price', ascending=False)

# Sort by multiple columns
sorted_df = pizza_sales_df.sort_values(['pizza_category_id', 'total_price'], ascending=[True, False])

# Groubp by pizza size id and get the count of sales (row count)
grouped_df_pizza_size = pizza_sales_df.groupby(['pizza_size_id']).count()

# Group by pizza size id and get the sum
grouped_df_pizza_size_by_sum = pizza_sales_df.groupby(['pizza_size_id'])['total_price'].sum()

# Group by pizza side id and sum total_price and quantity
grouped_df_pizza_size_sales_quantity = pizza_sales_df.groupby(['pizza_size_id'])[['total_price', 'quantity']].sum()

# Looking at different aggregation functions

#count(): Counts the number of non-NA/null values in each group.
#sum(): Sums the values in each group.
#mean(): Calculates the mean of values in each group.
#std(): Computes the standard deviation in each group.
#var(): Computes the standard variance in each group.
#min(): Finds the minimum values in each group.
#max(): Finds the maximum values in each group.
#prod(): Computes the product of values in each group.
#first(), last(): Gets the first and last values in each group.
#size(): Returns the size of each group (including NaN/NA values).
#nunique(): Counts the number of unique values in each group.


grouped_df_agg = pizza_sales_df.groupby(['pizza_size_id'])[['total_price', 'quantity']].sum()

# Using agg to perform different aggregations on different columns
aggregated_data = pizza_sales_df.groupby(['pizza_size_id']).agg({'quantity' : 'sum', 'total_price' : 'mean'})

# Merging pizza sales df and pizza size df
merged_df = pd.merge(pizza_sales_df, pizza_size_df, on='pizza_size_id')
# Add category information
merged_df = pd.merge(merged_df, pizza_category_df, on = 'pizza_category_id')

# Concatenate two dataframes - appending rows to a dataframe - vertically
another_pizza_sales_df = pd.read_excel('another_pizza_sales.xlsx')
concatenate_vertically = pd.concat([pizza_sales_df, another_pizza_sales_df], axis=0)
concatenate_vertically = concatenate_vertically.reset_index()

# Concatenate two dataframes - appending columns to a dataframe - horizontally
pizza_sales_voucher_df = pd.read_excel('/Users/devashanaidoo/Desktop/Python Course/Data/Pizza Sales Project/pizza_sales_voucher.xlsx')
concatenate_horizontally = pd.concat([pizza_sales_df, pizza_sales_voucher_df], axis = 1)

# Converting to lower case
lower_text = pizza_sales_df['pizza_ingredients'].str.lower()
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.lower()
# Convert to uppercase
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.upper()
# Converting to title case
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.title()

# Replacing text values
replaced_text = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', 'Mozzarella')
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', 'Mozzarella')

# Removing extra whitespaces
pizza_sales_df['pizza_name'] = pizza_sales_df['pizza_name'].str.strip()

# Generating a box plot

sns.boxplot(x='category', y='total_price', data=merged_df)
plt.xlabel('Pizza Category')
plt.ylabel('Total Sales')
plt.title('Boxplot showing distribution of sales by category')
plt.show()



































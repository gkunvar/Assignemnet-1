import numpy as np
import pandas as pd
import re

df1 = pd.read_csv('df_1.csv')
df2 = pd.read_csv('df_2.csv')

def clean_text(text):
    # Remove special characters and digits
    text_cleaned = re.sub(r'[^a-zA-Z\s]', '', text)  # Keeps only letters and spaces
    # Remove spaces
    text_cleaned = text_cleaned.replace(' ', '')
    # Convert to uppercase
    text_cleaned = text_cleaned.upper()
    return text_cleaned

dfc1 = df1['RM'].apply(clean_text)
dfc2 = df2['RM'].apply(clean_text)


# Merge the first columns
merged_column = pd.concat(dfc1, dfc2)

# Get unique values from the merged column
unique_values = merged_column.unique()

dfmerge_full = pd.merge()
dfunique_values = dfmerge_full.drop_duplicates

print(dfunique_values)
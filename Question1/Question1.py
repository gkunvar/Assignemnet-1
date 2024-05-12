import numpy as np
import pandas as pd
import re

df1 = pd.read_csv('df_1.csv')
df2 = pd.read_csv('df_2.csv')

def clean_text(text):
    # Remove special characters and digits
    text_cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Keeps only letters and spaces
    # Convert to uppercase
    text_cleaned = text_cleaned.upper()
    return text_cleaned

dfc1 = df1['RM'].apply(clean_text).str.strip()
dfc2 = df2['RM'].apply(clean_text).str.strip()

df_allValues = pd.concat([dfc1,dfc2])
unique_series = df_allValues.unique()
count_unique_values = len(unique_series)

print(count_unique_values)
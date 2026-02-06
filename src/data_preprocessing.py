import pandas as pd
import numpy as np

def load_data(filepath):
    """
    Load data from a CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}")
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None

def clean_data(df):
    """
    Perform basic data cleaning.
    """
    # Example cleaning steps based on notebook analysis
    # Standardize Gender
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].replace({'Femal': 'Female', 'Femle': 'Female'})
    
    # Fill missing values if any (placeholder)
    # df.fillna(0, inplace=True)
    
    return df

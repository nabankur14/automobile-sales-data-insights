import pandas as pd
import numpy as np
import os

def load_data(filepath):
    """Loads the dataset from the specified filepath."""
    if not os.path.exists(filepath):
        try:
            # Fallback for relative paths if run from different pwd
            base_dir = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(base_dir, filepath)
            if not os.path.exists(filepath):
                raise FileNotFoundError(f"File at {filepath} not found.")
        except Exception:
             raise FileNotFoundError(f"File at {filepath} not found.")
        
    return pd.read_csv(filepath)

def fill_partner_salary(row):
    """
    Fills missing Partner_salary.
    If Partner_working is 'No', returns 0.
    Else, returns Total_salary - Salary.
    """
    if row['Partner_working'] == 'No':
        return 0
    else:
        return row['Total_salary'] - row['Salary']

def clean_data(df):
    """
    Performs data cleaning steps:
    1. Replaces incorrect Gender values.
    2. Fills missing Gender values.
    3. Fills missing Partner_salary.
    """
    # Fix Gender typos
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].replace({"Femal": "Female", "Femle": "Female"})
        df['Gender'].fillna('Unknown', inplace=True)
    
    # Fill missing Partner_salary
    if 'Partner_salary' in df.columns and 'Partner_working' in df.columns and 'Total_salary' in df.columns and 'Salary' in df.columns:
        df['Partner_salary'].fillna(df.apply(fill_partner_salary, axis=1), inplace=True)
    
    return df

def preprocess_data(filepath):
    """Loads and cleans the data."""
    df = load_data(filepath)
    df = clean_data(df)
    return df

if __name__ == "__main__":
    # Example usage
    # Assuming the script is run from the root of the repo or src
    data_path = '../data/raw/automobile.csv' 
    try:
        df = preprocess_data(data_path)
        print("Data loaded and cleaned successfully.")
        print(df.info())
    except Exception as e:
        print(f"Error: {e}")

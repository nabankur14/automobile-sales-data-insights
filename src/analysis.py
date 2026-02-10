import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Ensure src can be imported if running this script directly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from data_preprocessing import preprocess_data
except ImportError:
    from src.data_preprocessing import preprocess_data

def plot_categorical_distributions(df, output_dir='../visuals'):
    """Plots univariate distributions for categorical columns."""
    categorical_columns = ['Gender', 'Profession', 'Marital_status', 'Education', 
                           'Personal_loan', 'House_loan', 'Partner_working', 'Make']
    
    os.makedirs(output_dir, exist_ok=True)
    
    for column in categorical_columns:
        if column in df.columns:
            plt.figure(figsize=(10, 5))
            sns.countplot(x=df[column])
            plt.title(f'Distribution of {column}')
            plt.savefig(os.path.join(output_dir, f'distribution_{column}.png'))
            plt.close()

def analyze_gender_make_preference(df, output_dir='../visuals'):
    """Analyzes and plots gender preference for different car makes."""
    if 'Make' in df.columns and 'Gender' in df.columns:
        print("\nGender preferences for Car Makes (Normalized %):")
        print(df.groupby(['Make'])['Gender'].value_counts(normalize=True)*100)
        
        plt.figure(figsize=(10, 5))
        sns.countplot(data=df, x='Make', hue='Gender')
        plt.title('Car Make vs Gender')
        plt.savefig(os.path.join(output_dir, 'make_by_gender.png'))
        plt.close()

def analyze_amount_spent_by_gender(df, output_dir='../visuals'):
    """Analyzes the amount spent on purchasing automobiles by gender."""
    # Based on the EDA plan, answering 'How does the amount spent... vary by gender?'
    # We can use Price column.
    if 'Price' in df.columns and 'Gender' in df.columns:
        plt.figure(figsize=(10,5))
        sns.boxplot(x='Gender', y='Price', data=df)
        plt.title('Amount Spent (Price) by Gender')
        plt.savefig(os.path.join(output_dir, 'price_by_gender.png'))
        plt.close()

def run_analysis():
    # Adjust path assuming run from root or src
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # goes up to repo root
    data_path = os.path.join(base_dir, 'data', 'raw', 'automobile.csv')
    output_dir = os.path.join(base_dir, 'visuals')
    
    print(f"Loading data from {data_path}...")
    
    try:
        df = preprocess_data(data_path)
        print("Data loaded and cleaned.")
        
        print(f"Generating visuals in {output_dir}...")
        plot_categorical_distributions(df, output_dir)
        analyze_gender_make_preference(df, output_dir)
        analyze_amount_spent_by_gender(df, output_dir)
        
        print("Analysis complete.")
    except Exception as e:
        print(f"Error during analysis: {e}")

if __name__ == "__main__":
    run_analysis()

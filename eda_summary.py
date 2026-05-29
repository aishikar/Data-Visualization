import pandas as pd
import numpy as np
from data_loader import DataPipeline

def run_initial_eda():
    print("Initializing Week 1 EDA Pipeline...")
    pipeline = DataPipeline(data_dir='data/')
    
    try:
        student_responses = pipeline.load_survey_data('COVID-19 Survey Student Responses.csv')
        
        summary = pipeline.get_basic_summary(student_responses)
        print(f"\nDataset Dimensions: {summary['shape'][0]} rows, {summary['shape'][1]} columns")
        
        print("\nInitial Column Overview:")
        for col in summary['columns'][:5]: # Screen first few features
            unique_count = student_responses[col].nunique()
            print(f" - Feature '{col}': {unique_count} unique values")
            
    except FileNotFoundError as e:
        print(f"Data loading notice: {e}")
        print("Ensure raw survey CSV files are placed inside the 'data/' directory.")

if __name__ == "__main__":
    run_initial_eda()

import pandas as pd
import numpy as np
from data_loader import DataPipeline

class DataMergerPipeline:
    def __init__(self):
        self.pipeline = DataPipeline(data_dir='data/')

    def build_integrated_dataset(self):
        print("Starting Week 2 Data Integration & Feature Engineering Pipeline...")
        
        try:
            df_students = self.pipeline.load_survey_data('COVID-19 Survey Student Responses.csv')
            
            df_students.columns = df_students.columns.str.strip()

            print(f"Base data shape: {df_students.shape}")

            print("Engineering new behavioral delta features...")
            
            if 'Time spent on Online Class' in df_students.columns and 'Time spent on self study' in df_students.columns:
                class_time = pd.to_numeric(df_students['Time spent on Online Class'], errors='coerce').fillna(0)
                study_time = pd.to_numeric(df_students['Time spent on self study'], errors='coerce').fillna(0)
                
                df_students['Total_Digital_Screen_Time'] = class_time + study_time
                print(" - Successfully generated feature: 'Total_Digital_Screen_Time'")

            df_responses = self.pipeline.load_survey_data('responses.csv')
            df_responses.columns = df_responses.columns.str.strip()

            master_df = df_students.merge(df_responses, left_index=True, right_index=True, how='left', suffixes=('_student', '_response'))
            
            print(f"Master integrated dataset created. Final Shape: {master_df.shape}")

            master_df.to_csv('data/integrated_master_dataset.csv', index=False)
            print("Saved combined baseline data to 'data/integrated_master_dataset.csv'")
            
            return master_df

        except FileNotFoundError as e:
            print(f"Data merge warning: {e}")
            print("Please confirm your data/ folder contains all target survey files.")

if __name__ == "__main__":
    merger = DataMergerPipeline()
    merger.build_integrated_dataset()

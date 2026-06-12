import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

class TrendAnalyzer:
    def __init__(self, master_data_path='data/integrated_master_dataset.csv'):
        self.data_path = master_data_path
        self.output_dir = 'results/'
        
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def run_statistical_analysis(self):
        print("Starting Week 3 Statistical Modeling & Visualization Pipeline...")
        
        if not os.path.exists(self.data_path):
            print(f"Data notice: '{self.data_path}' not found. Generating a baseline simulation for structural demonstration.")
        
            np.random.seed(42)
            df = pd.DataFrame({
                'Total_Digital_Screen_Time': np.random.normal(6, 2, 500),
                'Time spent on self study': np.random.normal(4, 1.5, 500),
                'Age of subject': np.random.randint(12, 25, 500)
            })
        else:
            df = pd.read_csv(self.data_path)
        
        # 1. Statistical Analysis
        print("Computing numerical feature correlation matrices...")
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 1:
            corr_matrix = df[numeric_cols].corr()
            print("\n--- Core Statistical Correlation Matrix ---")
            print(corr_matrix.round(4))
            
            # 2. Advanced Trend Visualization
            plt.figure(figsize=(8, 6))
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
            plt.title('COVID-19 Student Metrics: Feature Correlation Heatmap')
            plt.tight_layout()
            
            heatmap_path = os.path.join(self.output_dir, 'feature_correlation_heatmap.png')
            plt.savefig(heatmap_path)
            plt.close()
            print(f"--> Saved trend plot to: {heatmap_path}")
        else:
            print("Insufficient numerical features found for a robust correlation profile.")

        # 3. Aggregated Behavioral Grouping
        if 'Region of residence' in df.columns and 'Total_Digital_Screen_Time' in df.columns:
            print("\nCalculating screen-time metrics grouped by geographical region...")
            regional_summary = df.groupby('Region of residence')['Total_Digital_Screen_Time'].mean().reset_index()
            print(regional_summary.to_string(index=False))

        print("\nWeek 3 trend analysis loop completed successfully.")

if __name__ == "__main__":
    analyzer = TrendAnalyzer()
    analyzer.run_statistical_analysis()

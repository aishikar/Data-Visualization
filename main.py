import sys
from eda_summary import run_initial_eda
from data_merger import DataMergerPipeline
from trend_analyzer import TrendAnalyzer

def run_entire_pipeline():
    print("==========================================================")
    print("STARTING END-TO-END COVID-19 EDUCATION IMPACT PIPELINE")
    print("==========================================================\n")
    
    print("[STEP 1/3] Launching Data Cleansing & Exploratory Analysis...")
    run_initial_eda()
    print("-" * 50)
    
    print("[STEP 2/3] Launching Cross-Dataset Merging & Transformation...")
    merger = DataMergerPipeline()
    merger.build_integrated_dataset()
    print("-" * 50)
    
    print("[STEP 3/3] Launching Statistical Correlation & Chart Export...")
    analyzer = TrendAnalyzer()
    analyzer.run_statistical_analysis()
    
    print("\n==========================================================")
    print("PIPELINE EXECUTION COMPLETE: ALL ARTIFACTS EXPORTED SAFELY")
    print("==========================================================")

if __name__ == "__main__":
    run_entire_pipeline()

# Multi-Source Analysis: COVID-19 Impact on Global Education

## Project Overview
This project establishes an analytical pipeline to investigate how the COVID-19 pandemic reshaped student life, learning modalities, and mental routines. By combining multiple independent survey datasets and student metrics, this framework uncovers overarching socio-educational shifts through robust statistical tracking and data visualization.

## Project Development Lifecycle

### Week 1: Data Cleansing & Exploratory Analysis
- **Environment Layout:** Formulated a modular script structure separating data loading constraints from evaluation methods.
- **Exploratory Profiling:** Mapped row/column dimensions, missing attribute indices, and unique feature frequencies across student survey inputs.
- **Inconsistency Handling:** Standardized column types and structured raw inputs for multi-source mapping.

### Week 2: Feature Engineering & Dataset Merging (Current)
- **Schema Alignment:** Mapped cross-dataset intersections to determine consistent relational join parameters.
- **Pipeline Integration:** Created `data_merger.py` to systematically combine independent source survey logs without compromising row integrity.
- **Feature Generation:** Engineered explicit composite variables tracking total student digital exposure (`Total_Digital_Screen_Time`).
- **Validation:** Deployed integrity checks monitoring row-inflation or unintended null injection across join processes.

## Repository Structure
* `data/`: Local directory housing raw multi-source survey CSV files and intermediate integrated outputs.
* `data_loader.py`: Core utility class managing safe parsing boundaries for dataset ingestion.
* `data_merger.py`: Functional execution script managing tabular merge rules and feature transformations.
* `eda_summary.py`: Script evaluating preliminary feature metadata structures and array distributions.

## How to Run
1. **Dependencies:** Ensure standard analytics packages are configured:
   ```bash
   pip install pandas numpy matplotlib seaborn

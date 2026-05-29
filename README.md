# Multi-Source Analysis: COVID-19 Impact on Global Education

## Project Overview
This project establishes an analytical pipeline to investigate how the COVID-19 pandemic reshaped student life, learning modalities, and mental routines. By combining multiple independent survey datasets and student metrics, this framework uncovers overarching socio-educational shifts through robust statistical tracking and data visualization.

## Project Development Lifecycle

### Week 1: Data Cleansing & Exploratory Analysis (Current)
- **Environment Layout:** Formulated a modular script structure separating data loading constraints from evaluation methods.
- **Exploratory Profiling:** Mapped row/column dimensions, missing attribute indices, and unique feature frequencies across student survey inputs.
- **Inconsistency Handling:** Standardized column types and structured raw inputs for future multi-source mapping.

## Repository Structure
* `data/`: Local repository containing raw survey dataset CSV tables.
* `data_loader.py`: Functional class engine specialized in parsing tabular file assets safely.
* `eda_summary.py`: Analytical script computing descriptive distribution metrics and statistical shapes.

## How to Run
1. **Dependencies:** Ensure standard analytics packages are configured:
   ```bash
   pip install pandas numpy matplotlib seaborn

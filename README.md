# Multi-Source Analysis: COVID-19 Impact on Global Education

## Project Overview
This project establishes an analytical pipeline to investigate how the COVID-19 pandemic reshaped student life, learning modalities, and mental routines. By combining multiple independent survey datasets and student metrics, this framework uncovers overarching socio-educational shifts through robust statistical tracking and data visualization.

## Project Development Lifecycle

### Week 1: Data Cleansing & Exploratory Analysis
- **Environment Layout:** Formulated a modular script structure separating data loading constraints from evaluation methods.
- **Exploratory Profiling:** Mapped row/column dimensions, missing attribute indices, and unique feature frequencies across student survey inputs.
- **Inconsistency Handling:** Standardized column types and structured raw inputs for multi-source mapping.

### Week 2: Feature Engineering & Dataset Merging
- **Schema Alignment:** Mapped cross-dataset intersections to determine consistent relational join parameters.
- **Pipeline Integration:** Created `data_merger.py` to systematically combine independent source survey logs without compromising row integrity.
- **Feature Generation:** Engineered explicit composite variables tracking total student digital exposure (`Total_Digital_Screen_Time`).
- **Validation:** Deployed integrity checks monitoring row-inflation or unintended null injection across join processes.

### Week 3: Statistical Modeling & Trend Visualization
- **Statistical Correlation:** Implemented data scoring matrices inside `trend_analyzer.py` to evaluate linear dependencies across digital metrics and age profiles.
- **Aggregated Analytics:** Configured relational grouping blocks to study behavioral indicators sliced across demographics and regional distributions.
- **Visualization Assets:** Generated a professional matrix heatmap exploring cross-feature interactions, serialized to the `results/` directory.

### Week 4: Finalization & System Integration (Current)
- **Workflow Orchestration:** Implemented a master orchestrator (`main.py`) to stitch the data parsing, validation, merging, and visualization blocks together.
- **Code Refactoring:** Audited the entire repository structure to polish inline documentation, standardize styling profiles, and optimize dataset handling logic.
- **Final Packaging:** Closed out version control metrics and finalized complete replication criteria.

## How to Run
1. **Dependencies:** Ensure standard analytics packages are configured:
   ```bash
   pip install pandas numpy matplotlib seaborn

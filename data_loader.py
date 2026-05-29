import pandas as pd
import os

class DataPipeline:
    def __init__(self, data_dir='data/'):
        self.data_dir = data_dir

    def load_survey_data(self, filename):
        """Loads a specific CSV file from the data directory safely."""
        path = os.path.join(self.data_dir, filename)
        if not os.path.exists(path):
            raise FileNotFoundError(f"Target data file not found at: {path}")
        print(f"Successfully loaded: {filename}")
        return pd.read_csv(path)

    def get_basic_summary(self, df):
        """Returns fundamental structural dimensions and column metrics."""
        return {
            "shape": df.shape,
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict()
        }

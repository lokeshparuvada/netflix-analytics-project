import pandas as pd
import os


def load_data(file_path):

    extension = os.path.splitext(file_path)[1]

    if extension == ".csv":
        return pd.read_csv(file_path)

    elif extension == ".json":
        return pd.read_json(file_path)

    elif extension == ".xlsx":
        return pd.read_excel(file_path)

    else:
        raise ValueError("Unsupported format")
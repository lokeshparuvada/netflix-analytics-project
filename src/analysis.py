import pandas as pd
from src.database import create_connection


def run_query(query):

    mycon = create_connection()

    df = pd.read_sql_query(query, mycon)

    mycon.close()

    return df
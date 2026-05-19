import sqlite3
import os

# ensure database folder exists
os.makedirs("database", exist_ok=True)

DB_PATH = os.path.join("database", "netflix.db")


def create_connection():
    return sqlite3.connect(DB_PATH)


def create_table():
    mycon = create_connection()
    cursor = mycon.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS netflix_data (
        show_id TEXT,
        type TEXT,
        title TEXT,
        director TEXT,
        "cast" TEXT,
        country TEXT,
        date_added TEXT,
        release_year INTEGER,
        rating TEXT,
        duration TEXT,
        listed_in TEXT,
        description TEXT
    )
    """)

    mycon.commit()
    mycon.close()
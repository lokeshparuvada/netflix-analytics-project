from src.database import create_connection


def insert_data(df):
    mycon = create_connection()
    cursor = mycon.cursor()

    cursor.executemany("""
        INSERT INTO netflix_data (
            show_id, type, title, director, "cast",
            country, date_added, release_year,
            rating, duration, listed_in, description
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """, [tuple(row) for row in df.itertuples(index=False)])

    mycon.commit()
    mycon.close()
def clean_data(df):

    df = df.drop_duplicates()

    df["director"] = df["director"].fillna("Unknown")
    df["cast"] = df["cast"].fillna("Unknown")
    df["country"] = df["country"].fillna("Unknown")

    df = df.dropna(subset=["release_year", "type"])

    return df
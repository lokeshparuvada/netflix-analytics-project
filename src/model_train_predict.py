import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


def model_train_predict(df, future_year):

    # SORT DATA (important for time trend)
    df = df.sort_values("release_year")

    # FEATURE ENGINEERING (IMPROVEMENT)
    df["year_index"] = df["release_year"] - df["release_year"].min()

    X = df[["release_year", "year_index"]]
    y = df["total"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # MODEL (slightly improved tuning)
    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=6,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_test_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_test_pred)

    # FUTURE INPUT (IMPORTANT FIX)
    future_df = pd.DataFrame({
        "release_year": [future_year],
        "year_index": [future_year - df["release_year"].min()]
    })

    future_pred = model.predict(future_df)

    return int(future_pred[0]), round(r2, 2)
from src.database import create_table
from src.data_load import load_data
from src.data_cleaning import clean_data
from src.query import insert_data
from src.analysis import run_query
from src.visualization import plot_graph
from src.model_train_predict import model_train_predict


create_table()

df = load_data("Data/netflix_titles.csv")
df = clean_data(df)

insert_data(df)


query1 = """
SELECT release_year,
       type,
       COUNT(*) AS total
FROM netflix_data
GROUP BY release_year, type
ORDER BY release_year
"""

tv_query = """
SELECT release_year,
       COUNT(*) AS total
FROM netflix_data
WHERE type = 'TV Show'
GROUP BY release_year
ORDER BY release_year
"""

movie_query = """
SELECT release_year,
       COUNT(*) AS total
FROM netflix_data
WHERE type = 'Movie'
GROUP BY release_year
ORDER BY release_year
"""


result = run_query(query1)
Tv_1 = run_query(tv_query)
movie_1 = run_query(movie_query)


plot_graph(result, "release_year", "total", "type")
plot_graph(Tv_1, "release_year", "total")
plot_graph(movie_1, "release_year", "total")


future_year = int(input("\nEnter future year: "))

tv_prediction, tv_r2 = model_train_predict(Tv_1, future_year)
movie_prediction, movie_r2 = model_train_predict(movie_1, future_year)


print("\n========== PREDICTION RESULTS ==========")

print("\nTV SHOW PREDICTION")
print("Predicted Value:", tv_prediction)
print("R2 Score:", tv_r2)

print("\nMOVIE PREDICTION")
print("Predicted Value:", movie_prediction)
print("R2 Score:", movie_r2)
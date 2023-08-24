import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

POSSIBLE_DATA_PATHS = [
    r"C:\Users\edgar1993a\Desktop\data_movies.tsv",
]
DELIMITER = '\t'

class IMDB():
    def __init__(self) -> None:
        self.read_data()

    def read_data(self):
        for path in POSSIBLE_DATA_PATHS:
            try:
                self.data = pd.read_csv(
                    filepath_or_buffer=path,
                    delimiter=DELIMITER,
                )
                return
            except pd.ParserError:
                print("Error during reading.")
            except FileNotFoundError:
                print("The file was not found.")

    def n_movies(self):
        rows = len(self.data)
        print(f"The dataset contains {rows} movies: {rows / 1e6} millions.")


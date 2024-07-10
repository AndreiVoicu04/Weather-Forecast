import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


def dataset_info(df: pd.DataFrame):
    """ TODO:
    """
    # printing info about dataframe
    print("dataframe info")
    df.info()

    # finding the number of null values in entire dataframe
    print("\nnumber of null values")
    print(df.isnull().sum())

    # finding the number of duplicated rows in entire dataframe
    print("\nnumber of duplicated rows")
    print(df.duplicated().sum())

    # finding the minimum temperature
    print("\nminimum temperature")
    print(df.min(axis=0)["temp_min"])

    # finding the maximum temperature
    print("\nmaximum temperature")
    print(df.max(axis=0)["temp_max"])

    # most common weather condition
    print("\nmost common weather condition")
    weather_values_count = df["weather"].value_counts()
    weather_values_count.sort_values(ascending=False)
    print(weather_values_count.index[0])


def temp_max_histplot(df: pd.DataFrame):
    """ TODO:
    """
    sns.histplot(data=df, x="temp_max")
    plt.show()


def temp_max_facegrid_lineplot(df: pd.DataFrame):
    """ TODO:
    """
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    grid = sns.FacetGrid(df, col="year")
    grid.map(sns.lineplot, "month", "temp_max")
    plt.show()

def precipitation_facegrid_scatterplot(df: pd.DataFrame):
    """ TODO:
    """
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    grid = sns.FacetGrid(df, col="year")
    grid.map(sns.scatterplot, "month", "precipitation")
    plt.show()

def weather_countplot(df: pd.DataFrame):
    """ TODO:
    """
    sns.countplot(data=df, x="weather")
    plt.show()


def weather_piechart(df: pd.DataFrame):
    """ TODO:
    """
    palette_color = sns.color_palette('bright')
    weather_count = df["weather"].value_counts()
    plt.pie(weather_count, labels=weather_count.index, colors=palette_color)
    plt.show()


def lr_predictor_random_split(dataframe: pd.DataFrame):
    """ TODO:
    """


def lr_predictor_default_split(dataframe: pd.DataFrame):
    """ TODO:
    """


def svr_predictor_default_split(dataframe: pd.DataFrame):
    """ TODO:
    """


def main():
    df = pd.read_csv('seattle-weather.csv')
    # dataset_info(df)
    # temp_max_histplot(df)
    # temp_max_facegrid_lineplot(df)
    # precipitation_facegrid_scatterplot(df)
    # weather_countplot(df)
    weather_piechart(df)

if __name__ == '__main__':
    main()

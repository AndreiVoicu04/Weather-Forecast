import pandas as pd


def dataset_info(dataframe: pd.DataFrame):
    """ TODO:
    """
    # printing info about dataframe
    print("dataframe info")
    dataframe.info()

    # finding the number of null values in entire dataframe
    print("\nnumber of null values")
    print(dataframe.isnull().sum())

    # finding the number of duplicated rows in entire dataframe
    print("\nnumber of duplicated rows")
    print(dataframe.duplicated().sum())

    # finding the minimum temperature
    print("\nminimum temperature")
    print(dataframe.min(axis=0)["temp_min"])

    # finding the maximum temperature
    print("\nmaximum temperature")
    print(dataframe.max(axis=0)["temp_max"])

    # most common weather condition
    print("\nmost common weather condition")
    weather_values_count = dataframe["weather"].value_counts()
    weather_values_count.sort_values(ascending=False)
    print(weather_values_count.index[0])


def temp_max_histplot(dataframe: pd.DataFrame):
    """ TODO:
    """


def temp_max_facegrid_lineplot(dataframe: pd.DataFrame):
    """ TODO:
    """


def precipitation_facegrid_scatterplot(dataframe: pd.DataFrame):
    """ TODO:
    """


def weather_countplot(dataframe: pd.DataFrame):
    """ TODO:
    """


def weather_piechart(dataframe: pd.DataFrame):
    """ TODO:
    """


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
    dataset_info(df)


if __name__ == '__main__':
    main()

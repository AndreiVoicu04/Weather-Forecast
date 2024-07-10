import random
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import SVR

def add_month_year(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df["date"])
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    return df


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
    df = add_month_year(df)

    grid = sns.FacetGrid(df, col="year")
    grid.map(sns.lineplot, "month", "temp_max")
    plt.show()


def precipitation_facegrid_scatterplot(df: pd.DataFrame):
    """ TODO:
    """
    df = add_month_year(df)

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


def lr_predictor_random_split(df: pd.DataFrame):
    """ TODO:
    """
    df = add_month_year(df)
    x = df[["precipitation", "temp_min", "wind", "month", "year", "date"]]
    y = df["temp_max"]

    test_percentage = random.uniform(0, 1)
    (x_train, x_test,
     y_train, y_test) = train_test_split(x, y,
                                         test_size=test_percentage,
                                         shuffle=False)
    linreg = LinearRegression().fit(x_train.drop('date', axis=1), y_train)
    prediction = linreg.predict(x_test.drop('date', axis=1))

    x_plot = np.array(x_test["date"])
    y_plot = np.array(y_test)
    prediction_plot = np.array(prediction)

    plt.plot(x_plot, y_plot, color='blue')
    plt.scatter(x_plot, y_plot, color='blue')

    plt.plot(x_plot, prediction_plot, color='red')
    plt.scatter(x_plot, prediction_plot, color='red')

    plt.show()

    print(f"train_percentage: {1 - test_percentage}")
    print(f"test_percentage: {test_percentage}")
    print(f"MSE: {mean_squared_error(y_test, prediction)}")
    print(f"r2: {r2_score(y_test, prediction)}")

def lr_predictor_default_split(df: pd.DataFrame):
    """ TODO:
    """
    df = add_month_year(df)
    x = df[["precipitation", "temp_min", "wind", "month", "year", "date"]]
    y = df["temp_max"]

    (x_train, x_test,
     y_train, y_test) = train_test_split(x, y,
                                         test_size=.11,
                                         shuffle=False)
    linreg = LinearRegression().fit(x_train.drop('date', axis=1), y_train)
    prediction = linreg.predict(x_test.drop('date', axis=1))

    x_plot = np.array(x_test["date"])
    y_plot = np.array(y_test)
    prediction_plot = np.array(prediction)

    plt.plot(x_plot, y_plot, color='blue')
    plt.scatter(x_plot, y_plot, color='blue')

    plt.plot(x_plot, prediction_plot, color='red')
    plt.scatter(x_plot, prediction_plot, color='red')

    plt.show()

    print(f"MSE: {mean_squared_error(y_test, prediction)}")
    print(f"r2: {r2_score(y_test, prediction)}")

def svr_predictor_default_split(df: pd.DataFrame):
    """ TODO:
    """
    df = add_month_year(df)
    x = df[["precipitation", "temp_min", "wind", "month", "year", "date"]]
    y = df["temp_max"]

    (x_train, x_test,
     y_train, y_test) = train_test_split(x, y,
                                         test_size=.11,
                                         shuffle=False)

    svr = SVR(kernel='linear')
    svr.fit(x_train.drop('date', axis=1), y_train)
    prediction = svr.predict(x_test.drop('date', axis=1))

    x_plot = np.array(x_test["date"])
    y_plot = np.array(y_test)
    prediction_plot = np.array(prediction)

    plt.plot(x_plot, y_plot, color='blue')
    plt.scatter(x_plot, y_plot, color='blue')

    plt.plot(x_plot, prediction_plot, color='red')
    plt.scatter(x_plot, prediction_plot, color='red')

    plt.show()

    print(f"MSE: {mean_squared_error(y_test, prediction)}")
    print(f"r2: {r2_score(y_test, prediction)}")

def main():
    df = pd.read_csv('seattle-weather.csv')
    # dataset_info(df)
    # temp_max_histplot(df)
    # temp_max_facegrid_lineplot(df)
    # precipitation_facegrid_scatterplot(df)
    # weather_countplot(df)
    # weather_piechart(df)
    # lr_predictor_random_split(df)
    # lr_predictor_default_split(df)
    svr_predictor_default_split(df)


if __name__ == '__main__':
    main()

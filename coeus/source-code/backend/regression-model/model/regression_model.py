# imports

from iexfinance.stocks import Stock, get_historical_data
import pandas as pd
import numpy as np
import quandl, math
import datetime

from sklearn import preprocessing, svm
from sklearn.model_selection import cross_validate
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib
import matplotlib.pyplot as plt

from datetime import datetime

import sys
import os
# import client selected ticker data
absolute_path  = "/Users/o/Sites/coeus/source-code/backend/regression-model/retrieve-data"
sys.path.append(os.path.abspath(absolute_path))

import retrieve_ticker_data as rtd

def main():

	def historical_data(ticker_instance):

		dates = [datetime(2015, 1, 1), datetime.today()]

		historical_data_df = get_historical_data(
												str(ticker_instance.ticker),
												dates[0],
												dates[1],
												output_format='pandas',
												token = "sk_2db5017408dd4101b05d411f9d7f44b9"
												)

		return historical_data_df

	ticker_instance = rtd.main()
	df = historical_data(ticker_instance)
	print(df)

	forecast = 30
	df = df[["close"]]
	df["label"] = df["close"].shift(-forecast)

	x = np.array(df.drop(["label"], 1))
	x = preprocessing.scale(x)

	x_forecast = x[-forecast:]
	x = x[:-forecast]

	y = np.array(df["label"])
	y = y[:-forecast]

	def linear_regression(x, y):

		# creating training and test sets
		x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

		linear_regression = LinearRegression()
		linear_regression.fit(x_train, y_train)

		return linear_regression, x_test, y_test, x_train, y_train

	linear_regression, x_test, y_test, x_train, y_train = linear_regression(x, y)

	prediction = linear_regression.predict(x_forecast)
	prediction = np.asarray(prediction)
	accuracy = linear_regression.score(x_train, y_train)

	return prediction, forecast, accuracy

if __name__ == "__main__":
	main()

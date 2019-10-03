#!/usr/bin/env python
#imports
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import Stock
from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib import style

import numpy as np
import pandas as pd

import mpld3
from mpld3 import fig_to_html

from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression

# import retrieve-ticker-data from retrieve-ticker-data
import os
import sys

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

	def manipulate_data(df):

		# create adj. close price array from df and dates
		ticker_historic_close = []
		corresponding_dates = []

		temp_dates = df["close"].index.values
		for i in range(0, len(temp_dates)):

			temp_date = pd.to_datetime(str(temp_dates[i]))
			#temp_array = []
			#temp_array.append(temp_date.strftime("%Y-%m-%d"))
			#corresponding_dates.append(temp_array)
			corresponding_dates.append(temp_date)

		for quote in df["close"]:
			#temp_array = []
			#temp_array.append(quote)
			#ticker_historic_close.append(temp_array)
			ticker_historic_close.append(quote)

		return [ticker_historic_close, corresponding_dates]

	manipulated_data = manipulate_data(df)

	def graph_historical_close(close_prices, dates, df):

		# plot moving average and historical adj. close prices
		fig = plt.figure(1, figsize = (10, 4))
		plot = fig.add_subplot(111)

		moving_average = df["close"].rolling(window = 5).mean()

		plot.plot(dates, close_prices, label = "Historical Adj. Close Prices")
		plot.plot(dates, moving_average, "r", label = "Moving Average")

		# set max and min for x, y axes
		y_min = sorted(close_prices)[0]
		y_max = sorted(close_prices)[len(close_prices)-1]

		padding_percentage = 0.10
		plot.axis([
					datetime(2014, 12, 1),
					datetime(2020, 1, 1),
					round(y_min) - round(y_min) * padding_percentage,
					round(y_max) + round(y_min) * padding_percentage
					])

		plot.set_xlabel("Date")
		plot.set_ylabel("Stock Adj. Closing Price ($ USD)")
		plot.set_title(ticker_instance.company_name + " (" + ticker_instance.ticker + ") - Overview")
		plot.legend()

		# output
		plt.savefig("historical_close_prices.png")
		html = mpld3.save_html(fig, "historical_close_prices.html")

	graph_historical_close(manipulated_data[0], manipulated_data[1], df)

	# for use in regression_prediction.py in dir interactive-graphs
	return df

if __name__ == "__main__":
	main()

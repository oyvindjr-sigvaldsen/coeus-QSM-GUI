#!/usr/bin/env python
# imports
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import Stock

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from datetime import datetime

import mpld3
from mpld3 import fig_to_html

# import prediction var from regression_model.py
import os, sys

absolute_path = "/Users/o/Sites/coeus/source-code/backend/regression-model/model"
sys.path.append(os.path.abspath(absolute_path))

import regression_model as regression

# import close_prices, dates, df from historical_close_prices.py in dir interactive-graphs
absolute_path = "/Users/o/Sites/coeus/source-code/backend/regression-model/retrieve-data"
sys.path.append(os.path.abspath(absolute_path))

import retrieve_ticker_data as rtd

def main():

	# prerequisites
	regression_prediction, forecast, accuracy = regression.main()
	print(forecast, accuracy)
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

	def graph_historical_close(
								close_prices,
								dates,
								regression_prediction,
								forecast,
								accuracy
								):

		# plot moving average and historical adj. close prices
		fig = plt.figure(1, figsize = (10, 4))
		plot = fig.add_subplot(111)

		plot.plot(dates, close_prices, label = "Historical Adj. Close Prices")
		plot.plot(dates[-30:], regression_prediction, label = "ML Linear Regression Prediction")

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
		plot.set_title(ticker_instance.company_name + " (" + ticker_instance.ticker + ") - ML Regression Analysis Predictions")

		properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		text_string = "Accuracy = " + accuracy + " ('n' = " + forecast + ")"

		plot.text(0.70, 0.10, text_string, transform=plot.transAxes, fontsize=14,
        verticalalignment='top', bbox=properties)

		plot.legend()

		# output
		plt.savefig("regression_prediction.png")
		html = mpld3.save_html(fig, "regression_prediction.html")

	graph_historical_close(
							manipulated_data[0],
							manipulated_data[1],
							regression_prediction,
							str(forecast),
							str(accuracy)
							)


if __name__ == "__main__":
	main()

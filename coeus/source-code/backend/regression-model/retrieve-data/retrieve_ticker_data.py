# imports
import mysql.connector
import sys
import os

# import Ticker() class function from ticker-class directory
absolute_path  = "/Users/o/Sites/coeus/source-code/backend/regression-model/retrieve-data/ticker-class"
sys.path.append(os.path.abspath(absolute_path))

from ticker_class import Ticker

def main():

	def retrieve_data():

		client_selected_ticker = mysql.connector.connect(
			host="37.48.87.59",
			user="project01",
			passwd="tkDq9aPQ6bp5",
			database="coeus"
		)

		cursor = client_selected_ticker.cursor()

		sql = "SELECT * FROM `client-selected-ticker`"
		cursor.execute(sql)
		ticker_data = cursor.fetchall()

		selected_ticker = ticker_data[cursor.rowcount-1]
		return selected_ticker

	retrieved_ticker = retrieve_data()

	ticker_instance = Ticker(
							retrieved_ticker[0],
							retrieved_ticker[1],
							retrieved_ticker[2],
							retrieved_ticker[3],
							retrieved_ticker[4]
	)

	return ticker_instance

if __name__ == "__main__":
	main()

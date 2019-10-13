# imports
from iexfinance.refdata import get_symbols

from prettytable import PrettyTable
from tqdm import tqdm
import numpy as np
import pdfkit
import os

# $d = /Sites/coeus/source-code/backend/tickers-table

def main():

	# prerequisits
	tickers_df = get_symbols(output_format="pandas")

	df_headers = list(tickers_df.columns.values)

	np.asarray(df_headers)

	def assemble_html_table(tickers_df):

		tickers_df = tickers_df[[
								df_headers[7],
								df_headers[5],
								df_headers[6],
								df_headers[2],
								df_headers[0],
								]]

		# rename df column headers
		tickers_df.columns = ["Ticker", "Company Name", "Country", "Exchange", "Currency"]

		html_table = tickers_df.to_html("tickers_table.html",
						 classes="",
						 border="",
						 justify="unset")

		def modify_html():

			with open("tickers_table.html", "r") as file:
				file_data = file.read()

			targets = [
						["""<table border="" class="dataframe">""", """<table id="tickers-table">"""],
						["<tr>", """<tr class="ticker-table-tr" onclick="on(this); display_progress_bar();">"""],
						["<thead>", """<thead id="tickers-table-head">"""]
						]

			# iterate and append
			for i in range(0, len(targets)):

				sub_array = targets[i];

				file_data = file_data.replace(sub_array[0], sub_array[1])

			with open("tickers_table.html", "w") as file:
				file.write(file_data)

		modify_html()

		# export html table as pdf
		pdfkit.from_file('tickers_table.html', 'tickers_table.pdf')

	assemble_html_table(tickers_df)

	def assemble_ascii_table(tickers_df):

		# format table of possible ticker symbols
		table = PrettyTable()
		table.field_names = ["ticker", "name", "region", "exchange", "currency"]

		table.align["name"] = "l"
		table.align["ticker"] = "l"

		# iterate through tickers_df and add_rows to table referenced above
		def iterate_append_df(table):

			# reset to non-formated df
			tickers_df = get_symbols(output_format="pandas")

			# clear terminal window
			clear = lambda: os.system("clear")
			clear()

			with tqdm(total=int(len(tickers_df)), ncols=1) as pbar:

				# format tqdm progress bar
				pbar.set_description("Fetching iexfinance API Data")

				for i in range(0, len(tickers_df)):

					row_values = [
								tickers_df.loc[i][7],
								tickers_df.loc[i][5],
								tickers_df.loc[i][6],
								tickers_df.loc[i][2],
								tickers_df.loc[i][0]
								]

					table.add_row(row_values)

					#update tqdm progress bar
					pbar.update(1)

		iterate_append_df(table)
		return table

	# print ascii_table to clear and view tickers_table as ascii table in terminal window

		#ascii_table = assemble_ascii_table(tickers_df)
		#print(ascii_table)

if __name__ == "__main__":
	main()

class Ticker:
	def __init__(self, ticker, company_name, country, exchange, currency):
		self.ticker = ticker
		self.company_name = company_name
		self.country = country
		self.exchange = exchange
		self.currency = currency

	def parameters(self):

		ticker_parameters = vars(ticker_instance)
		attributes = ticker_parameters.keys()

		for i in range(0, len(attributes)):
			print(attributes[i])
		return attributes

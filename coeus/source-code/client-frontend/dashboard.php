<!DOCTYPE html>
<html lang="en-US">
	<head>
		<meta charset="utf-8">
		<meta name="description" content="Coeus | Client Dashboard">
		<meta name="author" content="Øyvind Jr. Sigvaldsen">
		<meta name="viewport" content"width=device-width" initial-scale="1.0">

		<link rel="stylesheet" type="text/css" href="css/main.css">
		<link rel="stylesheet" type="text/css" href="css/graphs.css">

		<script type="text/javascript" src="javascript/process_progress_bar.js"></script>
		<script type="text/javascript" src="javascript/retrieve_client_ticker.js"></script>
		<script type="text/javascript" src="javascript/search_tickers_table.js"></script>
		<script src="http://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
		<title>Coeus | Client Dashboard</title>
	</head>
	<body>
		<header>
		</header>
		<main>
			<div id="progress-bar">
				<div id="bar"></div>
			</div>
			<div id="left-column">
				<ul id="view-ticker-overlay" onclick="off()"></ul>
				<input type="text" id="search-tickers-table-input" onkeyup="query_tickers_table()" placeholder="Search Entity Tickers...">
				<div id="responsive-tickers-table">
					<?php include("../backend/tickers-table/tickers_table.html")?>
				</div>
				<form target="_blank" method="get" action="../backend/tickers-table/tickers_table.pdf">
					<button class="download-button" type="submit">Download</button>
				</form>
			</div>
			<div id="right-column">
				<div id="top-right">
					<iframe id="historical-close-prices-graph"src="http://localhost/coeus/source-code/backend/interactive-graphs/historical-close-prices/historical_close_prices.html" scrolling="no"></iframe>
					<div class="top-right-button-wrapper">
					</div>
				</div>
				<div id="bottom-right">
					<iframe id="regression-prediction-graph" src="http://localhost/coeus/source-code/backend/interactive-graphs/regression-prediction/regression_prediction.html" scrolling="no"></iframe>
				</div>
			</div>
		</main>
		<footer>
		</footer>
	</body>
<html>

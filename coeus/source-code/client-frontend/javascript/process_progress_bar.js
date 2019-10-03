function display_progress_bar() {

	var progress_bar_element = document.getElementById("bar");
	var width = 1;

	function frame_progress_bar() {

		if (width >= 100) {

			clearInterval(id);
		} else {

			width++;
			progress_bar_element.style.width = width + '%';
		}

		console.log(width);

		if (width == 100) {

			$.ajax({
				type: "POST",
				url: "http://localhost/coeus/source-code/backend/interactive-graphs/historical-close-prices/historical_close_prices.html"
			});

			$.ajax({
				type: "POST",
				url: "http://localhost/coeus/source-code/backend/interactive-graphs/regression-prediction/regression_prediction.html"
			});

			document.location.reload(false);
		} else {
			;
		}
	}
	var id = setInterval(frame_progress_bar, 80);
}

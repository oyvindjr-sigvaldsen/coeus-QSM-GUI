class SelectedTicker {
	constructor(ticker, company_name, country, exchange, currency) {
		this.ticker = ticker;
		this.company_name = company_name;
		this.country = country;
		this.exchange = exchange;
		this.currency = currency;
	}
}

function set_cookie(cookie_name, cookie_value, expiration_days) {

	var date = new Date();
	date.setTime(date.getTime() + (expiration_days*24*60*60*1000));

	var expires = "expires="+ date.toUTCString();
	document.cookie = cookie_name + "=" + cookie_value + ";" + expires + ";path=/";
}

function on(event) {

	var selected_row_elements = event.getElementsByTagName("td");

	selected_ticker = new SelectedTicker(
										selected_row_elements[0].textContent,
										selected_row_elements[1].textContent,
										selected_row_elements[2].textContent,
										selected_row_elements[3].textContent,
										selected_row_elements[4].textContent
										);

	console.log(selected_ticker);

	var class_properties = [];

	for (var property in selected_ticker) {
		if (Object.prototype.hasOwnProperty.call(selected_ticker, property)) {

			class_properties.push(property);
			set_cookie(property, selected_ticker[property], 1)

			console.log(property);
			console.log(selected_ticker[property]);
		}
	}

	set_cookie("selected_ticker_properties", JSON.stringify(class_properties), 1);

	$.ajax({
		type: "POST",
		url: "http://localhost/coeus/source-code/backend/php/send_ticker_data.php"
	});
}

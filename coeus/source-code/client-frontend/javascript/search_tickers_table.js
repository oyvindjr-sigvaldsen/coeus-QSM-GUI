 function query_tickers_table() {

	 var input, filter, table, tr, td, query_value;

	 input = document.getElementById("search-tickers-table-input");
	 filter = input.value.toUpperCase();
	 table = document.getElementById("tickers-table");
	 tr = table.getElementsByTagName("tr");

	 for (var i = 0; i < tr.length; i++) {

    	td = tr[i].getElementsByTagName("td")[0];

    	if (td) {
      		query_value = td.textContent || td.innerText;

			if (query_value.toUpperCase().indexOf(filter) > -1) {
				tr[i].style.display = "";
			} else {
				tr[i].style.display = "none";
      }
    }
  }
}

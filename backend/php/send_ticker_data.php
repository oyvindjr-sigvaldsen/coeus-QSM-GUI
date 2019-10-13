<?php
include "mysql_connect_class.php";

$mysql_connect_instance = new mysql_connect(
											"37.48.87.59",
											"project01",
											"tkDq9aPQ6bp5",
											"coeus");

$connection = new mysqli($mysql_connect_instance->{"server_ip"},
						$mysql_connect_instance->{"username"},
						$mysql_connect_instance->{"password"},
						$mysql_connect_instance->{"database"});

if ($connection->connect_error) {
	die("Connection failed: " . $connection->connect_error);
}

$properties = json_decode($_COOKIE["selected_ticker_properties"], true);

for ($i=0; $i < count($properties); $i++) {
	${$properties[$i]} = $_COOKIE[$properties[$i]];
}

function execute_sql($sql, $connection) {

	if (mysqli_query($connection, $sql)) {
    	echo "new record created successfully";
	} else {
    	echo "Error: " . $sql . "<br>" . $connection->error;
	}

	$connection->close();
}

$sql = "INSERT INTO `client-selected-ticker` (ticker, company_name, country, exchange, currency)
VALUES ('$ticker', '$company_name', '$country', '$exchange', '$exchange')";

execute_sql($sql, $connection);

$output = shell_exec("php generate_graphs.php");
echo $output;
?>

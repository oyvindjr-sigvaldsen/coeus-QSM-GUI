<?php
class mysql_connect {

	public $server_ip;
	public $username;
	public $password;
	public $database;

	function __construct( $server_ip, $username, $password, $database ) {
		$this->server_ip = $server_ip;
		$this->username = $username;
		$this->password = $password;
		$this->database = $database;
	}

	function __toString() {
		$connection_attributes = array($this->server_ip, $this->username, $this->password, $this->database);
		return implode ($connection_attributes, PHP_EOL);
	}
}
?>

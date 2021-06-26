<?php

require_once("car.php");
require_once("UberX.php");
require_once("Account.php");

$uberX = new UberX("CVB123", new Account("Andres Herrera", "AND456"), "Chevrolet", "Spark");
$uberX->printDataCar();

$uberPool = new UberPool ("tyu567", new Account("Andrea Ferran", "AND123"), "Dodge", "Attitude");
$uberPool->printDataCar();
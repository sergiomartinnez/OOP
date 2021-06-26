<?php
    require_once('Car.php');
    class uberX extends Car{
        public $brand;
        public $model;

        public function __construct($license, $driver, $brand, $model)
        {

            parent::__construct($license,$driver);
            $this->brand = $brand;
            $this->model = $model;
        }

        public function printDataCar() {
            echo "License: $this->license 
                Driver: {$this->driver->name} 
                Document: {$this->driver->document}
                passengers: $this->passengers
                Model: $this->model
                Brand: $this->brand";
        }
    }
?>
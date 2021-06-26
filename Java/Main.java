class Main {
    public static void main(String[] args) {
       System.out.println("Hola Mundo");
       Uberx uberx = new Uberx("AMQ123", new Account("Andres Herrera", "And123"), "Chevrolet", "sonic");
       uberx.setPassenger(2);
       uberx.printDataCar();

       UberVan UberVan = new UberVan("FGH123", new Account ("Andres Jhonson", "ANJ145"));
       UberVan.setPassenger(6);  
       UberVan.printDataCar(); 
       
       
       //Car car2 = new Car("QWE567", new Account("Andrea Herrera", "ANDA876"));
       //car2.passenger = 3;
       //car2.printDataCar();
    }
}
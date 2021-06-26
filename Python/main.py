from car import Car
from account import Account

from car import Car
from payment import Payment
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car()
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "QWE567"
    car2.driver = "Martha"
    print(vars(car2))

    paypal = Payment()
    paypal.ident = 21231
    paypal.email = "email@gmail.com"
    print(vars(paypal))

    user = Account() 
    user.ident = 21222
    user.name = "usuario123"
    user.document = "S21K"
    user.email = "usuario@gmail.com"
    user.password = "contra123"
    print(vars(user))

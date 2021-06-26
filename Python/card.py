from payment import Payment

class Card(Payment):
    ident = int
    cardName = str
    cardNumber = int
    cvv = int
    expirationDate = int

    def __init__(self, id, cardName, cardNumber, cvv, expirationDate):
        super().__innit__(ident)
        self.cardName = cardName
        self.cardNumber = cardNumber
        self.cvv = cvv
        self.expirationDate = expirationDate
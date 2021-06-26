from payment import Payment

class paypal(Payment):
    ident = int
    email = str

    def __init__(self, ident, email):
        super().__init__(ident)
        self.email = email
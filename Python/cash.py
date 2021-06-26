from payment import Payment

class cash(Payment):
    ident = int

    def __init__(self, ident):
        super().__init__(ident)

    
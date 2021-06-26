from account import Account

class User(Account):
    def __init__ (self, ident, name, document, email, password):
        super().__init__(ident, name, document, email, password)

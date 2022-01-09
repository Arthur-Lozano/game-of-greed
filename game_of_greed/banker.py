class Banker:
    def __init__(self, shelved=0, balance=0):
        self.shelved = shelved
        self.balance = balance

    def shelf(self, scores):
        self.shelved += scores

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def clear_shelf(self):
        self.shelved = 0

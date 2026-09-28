class BankAccount:
    def __init__(self, owner, balance, card_number):
        self.owner = owner
        self._balance = balance
        self.__card_number = card_number

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, val):
        if val < 0:
            print("Balance manfiy bo'lishi mumkin emas!")
        else:
            self._balance = val

    def __str__(self):
        return f"Egasi: {self.owner}, Balance: {self.balance} so'm"

    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance}, '{self.__card_number}')"

account1 = BankAccount("Ali", 1000000, "8600123456789012")
account2 = BankAccount("Vali", 2000000, "9860123456789012")

print(account1)
print(account2)

print("Ali balance:", account1.balance)

account1.balance = 1500000
account2.balance = 2500000

print("Yangi Ali balance:", account1.balance)
print("Yangi Vali balance:", account2.balance)

account1.balance = -500000

print(repr(account1))
print(repr(account2))
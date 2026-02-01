class Wallet:
    def __init__(self):
        self.money = 0

    def add_money(self, amount):
        if amount > 0:
            self.money += amount

    def withdraw(self, amount):
        if amount <= self.money:
            self.money -= amount
        else:
            print("Fonduri insuficiente")
    def transfer(self, other_wallet, amount):
        if amount <= self.money:
            self.money -= amount
            other_wallet.money += amount

my_wallet = Wallet()
my_wallet.add_money(100)
my_wallet.add_money(50)

# print(my_wallet.money)


class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet()


user = User('Mihai')
user.wallet.add_money(100)

w1 = Wallet(100)
w2 = Wallet(300)


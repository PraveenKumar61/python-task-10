class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self._balance = balance   

    def deposit(self, amount):
        self._balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Not enough balance")

    def show_balance(self):
        print("Name:", self.name)
        print("Balance:", self._balance)


# Child class
class SavingsAccount(BankAccount):

    # method overriding
    def show_balance(self):
        print("Savings Account")
        print("Name:", self.name)
        print("Balance:", self._balance)


# Main Program
acc1 = SavingsAccount("Praveen", 3000)
acc2 = SavingsAccount("Pranay", 2000)

acc1.deposit(1000)
acc1.withdraw(500)

acc2.deposit(500)

acc1.show_balance()
acc2.show_balance()

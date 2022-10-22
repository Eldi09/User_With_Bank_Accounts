class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance, acc_holder):
        self.int_rate = int_rate
        self.balance = balance
        self.acc_holder = acc_holder
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"Your balance after withdraw: ${self.balance}")
        elif self.balance - amount >= -195:
            print("Insufficient funds: Charging a $5 fee")
            print("You can go up to -$200.")
            self.balance -= (amount + 5)
            print(f"Your balance after withdraw: ${self.balance}")
        else:
            print("You can not go more than -$200.")
        return self

    def display_account_info(self):
        print(f"{self.acc_holder.name} balance is ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += (self.int_rate * self.balance)
        return self

    @classmethod
    def allAcc(cls):
        for x in cls.accounts:
            print(f"Balance: ${x.balance}")


# account1 = BankAccount(0.2, 1500)
# account2 = BankAccount(0.15, 900)
# account3 = BankAccount(0.15, 2000)

# account1.deposit(100).deposit(20).deposit(80).withdraw(130).yield_interest()
# account2.deposit(15).deposit(50).withdraw(100).withdraw(30).withdraw(50).withdraw(100).yield_interest()
# account3.deposit(100).deposit(20).deposit(80).withdraw(130).yield_interest()

# BankAccount.allAcc()

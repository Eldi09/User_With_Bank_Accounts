from BankAccount import BankAccount


class User:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    
    def create_accout(self, acc_name, amount, int_rate):
        if acc_name == "savings":
            self.accounts["savings"] = BankAccount(int_rate, amount, eldi)
            print(f"Saving account was created, your balance ${self.accounts['savings'].balance}")
        elif acc_name == "checking":
            self.accounts["checking"] = BankAccount(int_rate, amount, eldi)
            print(f"Checking account was created, your balance ${self.accounts['checking'].balance}")
        else:
            print("This type of account can not be created!")
            print("You can create only 'Saving' or 'Checking' accounts.")
        return self


eldi = User("Eldi Necaj")
eldi.create_accout("savings", 100, .3)
eldi.create_accout("checking", 200, 0)
# eldi.accounts['savings'].withdraw(50)
# eldi.accounts['checking'].withdraw(500)
eldi.accounts['savings'].yield_interest()
print(f"User: {eldi.name}, Checking balance ${eldi.accounts['checking'].balance}")
print(f"User: {eldi.name}, Saving balance ${eldi.accounts['savings'].balance}")


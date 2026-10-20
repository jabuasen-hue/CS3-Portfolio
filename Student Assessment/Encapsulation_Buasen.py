class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("The balance must be not be a negative number.")
        else:
            self.__balance = value

print("Output:")
print("Account 1")
    
my_account = BankAccount(12345, 1000.00)
    
print(f"Account Number: {my_account.account_number}")
print(f"Balance: {my_account.balance:.2f}")
    
print("\nUpdate balance to -100")
my_account.balance = -100
    
print(f"Account Number: {my_account.account_number}")
print(f"Balance: {my_account.balance:.2f}")
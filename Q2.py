class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds. Withdrawal not allowed.")

    def get_balance(self):
        return self.balance

#taking input
account_number_input = input("Enter account number: ")
account_holder_input = input("Enter account holder's name: ")
initial_balance_input = float(input("Enter initial balance (optional, default is 0.0): "))

my_account = BankAccount(account_number_input, account_holder_input, initial_balance_input)
print(f"Account created for {my_account.account_holder} with account number {my_account.account_number}.")
print(f"Initial balance: {my_account.get_balance()}")

# deposit some money
deposit_amount = float(input("Enter amount to deposit: "))
my_account.deposit(deposit_amount)
print(f"Updated balance after deposit: {my_account.get_balance()}")

# withdraw some money
withdraw_amount = float(input("Enter amount to withdraw: "))
my_account.withdraw(withdraw_amount)
print(f"Updated balance after withdrawal: {my_account.get_balance()}")

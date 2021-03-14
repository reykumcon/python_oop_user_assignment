class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.name} transfer money to {other_user.name}... \nTransfer Amount: {amount}")

alice = User('Alice', 'alice@account.com')
ben = User('Ben', 'ben@account.com')
charlie = User('Charlie', 'charlie@account.com')

alice.make_deposit(10)
alice.make_deposit(20)
alice.make_deposit(30)
alice.make_withdrawal(10)
alice.display_user_balance()

ben.make_deposit(20)
ben.make_deposit(30)
ben.make_withdrawal(10)
ben.make_withdrawal(10)
ben.display_user_balance()

charlie.make_deposit(50)
charlie.make_withdrawal(10)
charlie.make_withdrawal(10)
charlie.make_withdrawal(10)
charlie.display_user_balance()

alice.transfer_money(charlie, 10)
alice.display_user_balance()
charlie.display_user_balance()

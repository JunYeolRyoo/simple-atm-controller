class Account:
    accounts = {}

    @classmethod
    def create_account(cls, account_number, pin, balance=0) -> object:
        if cls.check_account(account_number):
            account = cls(account_number,pin,balance)
            cls.accounts[account_number] = account
            return account
        else:
            raise ValueError("Account with number {} already exists.".format(account_number))
            
    @classmethod
    def check_account(cls,account_number) -> bool:
        return account_number not in cls.accounts
    
    def __init__(self, account_number, pin, balance=0) -> None:
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
    
    def check_pin(self,entered_pin) -> bool:
        return self.pin == entered_pin
    
    def get_balance(self) -> int:
        return self.balance
    
    def deposit(self, amount) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self,amount) -> bool:
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False
    
class ATM:
    def __init__(self) -> None:
        self.accounts = {}
        self.current_account = None

    def add_account(self, account) -> None:
        if account.account_number not in self.accounts:
            self.accounts[account.account_number] = account
    
    def insert_card(self, account_number) -> bool:
        if account_number in self.accounts:
            self.current_account = self.accounts[account_number]
            return True
        return False
    
    def enter_pin(self,pin) -> bool:
        if self.current_account and self.current_account.check_pin(pin):
            return True
        return False
    
    def see_balance(self) -> None:
        if self.current_account:
            print("Current balance: ${}".format(self.current_account.get_balance()))
    
    def deposit(self, amount) -> bool:
        if self.current_account:
            return self.current_account.deposit(amount)
        return False
    
    def withdraw(self,amount) -> bool:
        if self.current_account:
            return self.current_account.withdraw(amount)
        return False
    
    def eject_card(self) -> None:
        self.current_account = None



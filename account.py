import person
class BankAccount(person.PersonalInfo):
    def __init__(self, id: int, name: str, ph: int, email: str, balance: float):
        self.id = id
        self.name = name
        self.ph = ph
        self.email = email
        self.balance = balance

    def __str__(self) -> str:
        return f'{super().__str__()} Balance is:{self.balance}'

    def Withdraw(self, money: float):
        self.balance += self.balance - money

    def Deposit(self, money: float):
        self.balance += self.balance + money

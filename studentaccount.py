import account


class StudentBankAccount(account.BankAccount):
    def __init__(self, id: int, name: str, ph: int, email: str, balance: float, college_name: str):
        self.id = id
        self.name = name
        self.ph = ph
        self.email = email
        self.balance = balance
        self.college_name = college_name

    def __str__(self) -> str:
        return f'{super().__str__()} college_name:{self.college_name}'

    def Withdraw(self, money: float):
        self.balance += super().Withdraw(money)-super().Withdraw(money)*1.5

    def Deposit(self, money: float):
        self.balance += super().Deposit(money)-super().Deposit(money)*1.5
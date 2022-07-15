import account

class BusinessBankAccount(account.BankAccount):
    def __init__(self, id: int, name: str, ph: int, email: str, balance: float, business_info: str):
        if balance < 0: raise ValueError("Student can’t have negative balance ")
        self.id = id
        self.name = name
        self.ph = ph
        self.email = email
        self.balance = balance
        self.business_info = business_info

    def __str__(self) -> str:
        return f'{super().__str__()} business_info:{self.business_info}'

class PersonalInfo:
    def __init__(self,id:int,name:str,ph:int,email:str):
        self.id=id
        self.name = name
        self.ph = ph
        self.email = email

    def __str__(self) -> str:
        return f'id:{self.id} name:{self.name} Phone number:{self.ph} Email address:{self.email}'

class People:
    def __init__(self, name, age, cpf):
        self.name = name
        self.age = age
        self.cpf = cpf
        
    def display(self):
        return f"Name: {self.name}, Age: {self.age}, CPF: {self.cpf}"
    
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
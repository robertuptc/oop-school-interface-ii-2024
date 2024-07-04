class User:
    def __init__(self, name, age, id, password, role):
        self.name = name
        self.age = age
        self.id = id
        self.password = password
        self.role = role

    def __repr__(self):
        return f"{self.name} | {self.age} | {self.role} | {self.id} | {self.password}"
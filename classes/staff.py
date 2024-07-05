import csv
from .user import User

class Staff:
    @classmethod
    def load_all_staff(cls):
        all_staff = []
        with open('./data/staff.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_student = cls(**row)
                all_staff.append(new_student)
        return all_staff


    def __init__(self, name, age, employee_id, password, role=None):
        self.name = name
        self.age = age
        self.password = password
        self.employee_id = employee_id
        self.role = role
    
    # def __repr__(self):
    #     return f"{self.name} | {self.age} | {self.role}"
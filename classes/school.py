class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.staff = []
        
    def __rerp__(self):
        return f"{self.name}"

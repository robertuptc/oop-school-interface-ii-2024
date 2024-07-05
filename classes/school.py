class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.staff = []
        
    def __rerp__(self):
        return f"{self.name}"

    def list_students(self):
        print("-------------------------------\nSTUDENTS LIST\n-------------------------------")
        counter = 1
        for student in self.students:
            print(f"{counter}. {student.name} {student.id}")
            counter += 1
    
    def find_student_by_id(self, desired_school_id):
        desired_student = None
        for student in self.students:
            desired_student = None
            if int(student.school_id) == int(desired_school_id):
                desired_student = student
                break
        # error handling
        if desired_student is None:
            print(f"Student with school_id {desired_school_id} does not exist")
        else:
            print(desired_student)
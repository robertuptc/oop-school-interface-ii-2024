from classes.school import School
from classes.student import Student
from classes.staff import Staff

ridgemont_high = School('Ridgemont High') 
# print(ridgemont_high.name)

# robert = Student('robert', 33, 'password', 123)
# print(robert)

ridgemont_high.students = Student.load_all_students()
# print(ridgemont_high.list_students())

# triton = Staff('Triton', 5, "p123", 1)
# print(triton)

# ridgemont_high.staff = Staff.load_all_staff()
# print(ridgemont_high.staff)

# ridgemont_high.find_student_by_id(13345)

main_ui_message = f"""
{ridgemont_high.name} Student Interface
-------------------------------
Welcome, Richard. Your access level is Principal
What would you like to do?
Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit
"""
# Command line program
is_active = True
# is_active = False
while is_active:
    cmd = input(main_ui_message)
    # view all students
    if cmd == '1':
        ridgemont_high.list_students()

    # view student by id
    elif cmd == '2':
        desired_school_id = input("Enter Student ID you would like information for: ")
        ridgemont_high.find_student_by_id(desired_school_id)

    # add a student
    elif cmd == '3':
        info = input("Enter student info in the following format, separated by commas. Name, Age, School ID, Password: ")
        info = info.split(',')
        
        new_student = Student(info[0], info[1], info[2], info[3])
        print(new_student)

    # remove a student
    elif cmd == '4':
        id_to_del = input("Enter Student ID you would like to delete: ")
        updated_students = []
        for student in ridgemont_high.students:
            if student.school_id != id_to_del:
                updated_students.append(student)
        ridgemont_high.students = updated_students
        print(updated_students)

    # quit
    elif cmd == '5':
        is_active = False
    
    # error handling
    else:
        print("Invalid input")
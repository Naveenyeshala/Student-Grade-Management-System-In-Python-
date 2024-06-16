#initialisation
student_grades={}

# add a new student
def add_student(name,grade):

    student_grades[name]=grade
    
    print(f"added {name} with a {grade}")

#update a student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found!")

#delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been sucessfully deleted")
    else:
        print(f"{name} is not found!")

#view all students
def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found ")


def main():

    while True:
        
        print('\n Student Grades Management System')
        print("1.Add student")
        print("2.Update student")
        print("3.Delete student")
        print("4.view student")
        print("5. Exit")
        

        choice= int(input("Enter your choice= "))
        if choice == 1:
            name = input("Enter student name = ")
            grade = input("Enter student grade = ")
            add_student(name,grade)

        elif choice == 2:
            name = input("Enter student name = ")
            grade = input("Enter student grade = ")
            update_student(name,grade)
        
        elif choice == 3:
             name = input("Enter student name = ")
             delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break
        else:
            print("Invaild choice")

if __name__ == "__main__":
    main()

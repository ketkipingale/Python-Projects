
db=[]
class Student:
    def __init__(self,nm,roll,mk):
        self.name=nm
        self.roll=roll
        self.marks=mk
    def add_student(self):
        u_name=input("Enter your Name : ")
        u_roll=input("Enter your Roll Number : ")
        u_marks=input("Enter your Marks : ")
        s1=Student(u_name,u_roll,u_marks)
        db.append(s1)
        print("Student added in Database Successfully")
    def display_student(self,ob):
        print(f"Student Name is {ob.name}")
        print(f"Student Roll Number is {ob.roll}")
        print(f"Student marks are {ob.marks}")
        print('-'*50)
    def search_student(self):
        roll=input("Enter Your roll Number : ")
        for i in range(len(db)):
            if db[i].roll==roll:
                print("Student Found in Database")
                return i
    def delete_student(self):
        i=obj.search_student()
        del db[i]
        print("Student Deleted from Database Successfully")
        if len(db)==0:
            print("Database is Empty")
        print('-'*50)
    def update_student(self):
        i=obj.search_student()
        u_name=input("Enter Updated Name : ")
        u_roll=input("Enter Updated Roll Number : ")
        u_marks=input("Enter Updated Marks : ")
        db[i].name=u_name
        db[i].roll=u_roll
        db[i].marks=u_marks
        print("Student record successfully updated in Database")
        print('-'*50)
obj=Student('',0,0)
s1=Student('Pawan',101,77)
db.append(s1)
while 1:
    print('='*50)
    print('*****WELCOME TO STUDENT MANAGEMENT SYSTEM*****')
    print('='*50)
    print("""
                1. Add student
                2. Display student
                3. Search Student
                4. Delete Student
                5. Update Student
                6. Exit              """
    )
    print('*'*50)
    ch=int(input("Enter your choice : "))
    print('-'*50)
    if ch==1:
        obj.add_student()
    elif ch==2:
        for i in range(len(db)):
            obj.display_student(db[i])
    elif ch==3:
        if len(db)==0:
            print("No student in Database")
        else:
            i=obj.search_student()
    elif ch==4:
        obj.delete_student()
    elif ch==5:
        obj.update_student()
    elif ch==6:
        break
    else:
        print("Your choice is Invalid")

    print('-'*50)
    choice=input("Do you want to continue yes/no : ")
    choice=choice.lower()
    if choice=='yes':
        pass
    else: 
        break

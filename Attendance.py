from sklearn.linear_model import LogisticRegression
students = {}

X = [[90, 1],[85, 2],[80, 3],[70, 5],[65, 6],[60, 8],[95, 0],[50, 10]]
y = [0, 0, 0, 1, 1, 1, 0, 1]

model=LogisticRegression()
model.fit(X, y)


def add_student():
    name=input("Enter student name: ")
    roll=input("Enter roll number: ")

    students[roll]={"name":name,"present":0,"total":0,"leave":0}
    print("Student added successfully.")


def mark_attendance():
    roll=input("Enter roll number: ")

    if roll in students:
        status=input("Present or Absent (P/A):").upper()
        students[roll]["total"]+=1

        if status=="P":
            students[roll]["present"]+=1
            print("Attendance marked as Present.")
        else:
            print("Attendance marked as Absent.")
    else:
        print("Student not found.")


def apply_leave():
    roll=input("Enter roll number: ")

    if roll in students:
        days=int(input("Enter number of leave days: "))
        students[roll]["leave"]+=days
        print("Leave applied successfully.")
    else:
        print("Student not found.")


def check_attendance():
    roll=input("Enter roll number:")

    if roll in students:
        present=students[roll]["present"]
        total=students[roll]["total"]
        leave_days=students[roll]["leave"]

        if total==0:
            percentage=0
        else:
            percentage=(present / total)*100

        print("Student Name:",students[roll]["name"])
        print("Attendance Percentage:", round(percentage, 2),"%")

        prediction = model.predict([[percentage,leave_days]])

        if prediction[0]==1:
            print("AI Prediction: Student is at risk of attendance shortage")
        else:
            print("AI Prediction: Student attendance is safe")

        print()
    else:
        print("Student not found.")


def display_student_record():
    roll = input("Enter roll number:")

    if roll in students:
        data=students[roll]

        if data["total"]==0:
            percentage=0
        else:
            percentage=(data["present"]/data["total"])*100

        print("Student Record")
        print("Name:",data["name"])
        print("Roll Number:",roll)
        print("Present Classes:",data["present"])
        print("Total Classes:",data["total"])
        print("Leave Days:",data["leave"])
        print("Attendance Percentage:",round(percentage, 2),"%")
    else:
        print("Student not found.")


while True:
    print("1.Add Student")
    print("2.Mark Attendance")
    print("3.Apply Leave")
    print("4.Check Attendance with AI Prediction")
    print("5.Display Student Record")
    print("6.Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        add_student()
    elif choice=="2":
        mark_attendance()
    elif choice=="3":
        apply_leave()
    elif choice=="4":
        check_attendance()
    elif choice=="5":
        display_student_record()
    elif choice=="6":
        print("Exiting Program..")
        break
    else:
        print("Invalid choice.Please try again.")
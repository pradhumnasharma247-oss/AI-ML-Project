Smart Attendance Prediction and Leave Management System

Student Name:Pradhumna Sharma
Registration NO.:25MIM10066
Year:2nd Year
Course: Integrated Mtech (AI)


PROJECT TITLE
AI-Based Smart attendance predictor and leave management system for college students.


PROJECT OVERVIEW
This project is based on a common problem faced by many students in college. Most students do not keep checking their attendance regularly and later find out that they are below the minimum attendance requirement.
In many colleges, students need at least 75% attendance to sit in exams. If their attendance is too low, they may face shortage issues, stress, or may not be allowed to appear in exams.
Teachers also spend a lot of time managing attendance records manually. It can become difficult to track which students are safe and which students may face attendance shortage in the future.
To solve this problem,this project provides an AI-Based Smart Attendance Prediction and Leave Management System.
This system helps students and teachers manage attendance in a simple way. It can store attendance details, calculate attendance percentage, record leave days, and predict whether a student may face attendance shortage in the future.

PROBLEM STATEMENT
In many colleges, students struggle to maintain the minimum attendance required for exams. Most students only realize they are below 75% attendance when the semester is almost over. This creates stress, shortage issues, and sometimes even exam detention.
Teachers also spend a lot of time maintaining attendance records manually. It becomes difficult to predict which students are likely to face attendance shortage in the future.

Because of this,there is a need for a system that can help students track their attendance regularly and also predict whether they are at risk of low attendance before it becomes a serious problem.


OBJECTIVE OF THE PROJECT
The main objective of this project is to:
Maintain attendance records of students
Store leave details
Calculate attendance percentage
Predict attendance shortage using AI
Reduce manual work for teachers
Help students stay aware of their attendance status

SOLUTION EXPLANATION
To solve this problem, an AI-Based Smart Attendance Prediction and Leave Management System was developed using Python.
The system stores student details such as name, roll number, attendance records, and leave details.
Whenever attendance is marked, the system updates the total number of classes and the number of classes attended by the student.
The system then calculates the attendance percentage automatically.
If the attendance percentage is below 75%, the system gives a warning message.
Along with this, a Machine Learning model called Logistic Regression is used to predict whether the student may face attendance shortage in the future.
The prediction is based on:
Attendance Percentage
Number of Leave Days
If the attendance percentage is low and leave days are high, the system predicts that the student is at risk.
This makes the project more useful because students can take action early and improve their attendance before it becomes too late.

FEATURES OF THE PROJECT
1. Add Student Details
2. Mark Attendance
3. Apply for Leave
4. Calculate Attendance Percentage
5. Predict Future Attendance Shortage
6. Display Complete Student Record
7. Command Line Based Execution

TECHNOLOGIES USED
1. Python
2. Scikit-learn
3. Logistic Regression
4. Dictionaries
5. Loops
6. Functions
7. Conditional Statements

HOW THE PROJECT WORKS
First, the user enters student details like name and roll number.
Then attendance can be marked as Present or Absent.
If the student takes leave, the number of leave days can also be entered.
The system then calculates the attendance percentage of the student.
After that, the Machine Learning model checks the attendance percentage and leave days to predict whether the student is safe or at risk of attendance shortage.
For example:
If attendance is above 75%,the student is considered safe.
If attendance is below 75%,the system gives a warning message.
If leave days are high and attendance is low, the AI model predicts that the student is at risk.

MACHINE LEARNING USED
This project uses Logistic Regression,which is a simple Machine Learning algorithm.

The model is trained using sample data that contains:
Attendance Percentage
Number of Leave Days
Based on this information,the model predicts whether the student is:
Safe
At Risk of Attendance Shortage

DEPENDENCIES REQUIRED
The following library is required to run this project:
scikit-learn
Install it using the following command:
pip install scikit-learn

HOW TO RUN THE PROJECT
Step 1: Open terminal or command prompt.
Step 2: Go to the project folder.
Step 3: Run the Python file using:
Attendance.py

FILES INCLUDED IN THE PROJECT
1.Attendance.py
2.README.md
3.Project Report

LEARNING OUTCOME
Through this project,I had learned:
How to create a real-life project using Python
How to use Machine Learning in a simple project
How to use Logistic Regression
How to work with dictionaries and functions
How to create a menu-driven program
How to solve a real-world problem using technology

FUTURE IMPROVEMENTS
In the future,this project can be improved by:

Adding a database like MySQL
Adding login system for students and teachers
Adding graphical user interface
Adding subject-wise attendance tracking
Storing attendance permanently
Generating attendance reports automatically

CONCLUSION
This project is simple,useful,and based on a real problem faced by students and teachers in colleges.
It helps reduce manual work, saves time, and makes attendance tracking easier.
The use of Machine Learning makes the project more interesting because it can predict future attendance shortage and give an early warning to students.

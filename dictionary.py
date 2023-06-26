students=[]
numOfStudent=int(input("please enter total number of student"))

for i in range(numOfStudent):
    print("details of student", (i+1))
    student = {}
    student["name"] = input("please enter the name of student :")
    student["marks"] =int(input("please input the marks :"))
    students.append(student)
for i in range(numOfStudent):
    student_display=students[i]
    print("Sr. No =", [i+1])
    print("Name" , student_display["name"])
    print("marks" , student_display["marks"])
    





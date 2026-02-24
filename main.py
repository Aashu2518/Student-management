students = []

while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        students.append(input("Enter student name: "))
    elif ch == "2":
        print(students)
    elif ch == "3":
        students.remove(input("Name to delete: "))
    else:
        break

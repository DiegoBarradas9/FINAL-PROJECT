import string

class Student:
    def __init__(self, studentID, firstName, lastName, email, section):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.section = section
    
    def values(self):
        return ("{:<40} {:<40} {:<40} {:<40} {:<40}".format(self.studentID, self.firstName, self.lastName, self.email, self.section))

def printMenu():
    print('[1] ADD STUDENT')
    print('[2] SEARCH STUDENT')
    print('[3] EDIT STUDENT')
    print('[4] DELETE STUDENT')
    print('[5] SHOW ALL STUDENTS')
    print('[6] DISPLAY SECTIONS')
    print('[7] EXIT')

def addStudent():
    print("\n===| ADD STUDENT |===")
    print("**Please fill up the following credentials**")
    try:
        studentIdExists = False
        studentId = int(input('Student ID: '))

        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if str(studentId) in lines[n].split():
                    print('--------------------------------------------------------')
                    print('Student ID already exists!\n')
                    studentIdExists = True
                    break
                
        if not studentIdExists:
            firstName = input('Firstname: ')
            lastName = input('Lastname: ')
            email = input('Email: ') 

            print("\n===| Sections |===")
            print("[1] IT-2101")
            print("[2] IT-2102")
            print("[3] IT-2103")
            print("[4] IT-2104")
            print("[5] IT-2105")

            select = input("\nSelect Section: ")
            if select == "1":
                section = "IT-2101"
            elif select == "2":
                section = "IT-2102"
            elif select == "3":
                section = "IT-2103" 
            elif select == "4":
                section = "IT-2104"
            elif select == "5":
                section = "IT-2105"
            else:
                print("\nInvalid input\nPlease try again...\n")
                addStudent()

            student = Student(studentId,firstName,lastName,email,section)
            with open("StudentRecord.txt", "a") as myfile:
                myfile.write("\n")
                myfile.write(student.values())

            print('--------------------------------------------------------')
            print('Student Added Successfully!\n')

    except ValueError:
        print("Your input is not a valid option!\n")
   

def searchStudent():
    print("\n===| SEARCH STUDENT |===")
    choice = input("Search by \n[1] Lastname\n[2] Student ID #\nChoice: ")
    isFound = False
    foundStudents = [];
    if choice == '1':
        lastname = input('Enter lastname: ')
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if lastname == lines[n].split()[2]:
                    isFound = True
                    foundStudents.append(lines[n].split())
            if isFound:
                print('--------------------------------------------------------')
                print('Record Found!\n')
                print("{:<25} {:<25} {:<25} {:<25} {:<25}".format("Student ID", "Firstname", "Lastname", "Email", "Section"))
                for i in range(len(foundStudents)):
                    print("{:<25} {:<25} {:<25} {:<25} {:<25}".format(foundStudents[i][0],foundStudents[i][1],foundStudents[i][2],foundStudents[i][3],foundStudents[i][4]))
                print("")
                foundStudents.clear()
            else:
                print('--------------------------------------------------------')
                print("Student doesn't exist!\n")

    elif choice == '2':
        studentId = input('Enter Student ID #: ')
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for n in range(len(lines)):
                if studentId == lines[n].split()[0]:
                    isFound = True
                    foundStudents.append(lines[n].split())
            if isFound:
                print('--------------------------------------------------------')
                print('Record Found!\n')
                print("{:<25} {:<25} {:<25} {:<25} {:<25}".format("Student ID", "Firstname", "Lastname", "Email", "Section"))
                for i in range(len(foundStudents)):
                    print("{:<25} {:<25} {:<25} {:<25} {:<25}".format(foundStudents[i][0],foundStudents[i][1],foundStudents[i][2],foundStudents[i][3],foundStudents[i][4]))
                    print("")
                foundStudents.clear()
            else:
                print('--------------------------------------------------------')
                print("Student doesn't exist!\n")
        
    else:
        print('--------------------------------------------------------')
        print("Invalid choice!\n")
        

def editStudent():
    print("\n===| EDIT STUDENT |===")
    studID = input("Enter Student ID #: ")
    isFound = False
    with open("StudentRecord.txt", "r") as fp:
        lines = fp.readlines()
        for n in range(len(lines)):
            record = lines[n].split()
            if len(record) != 0:
                if studID == record[0]:
                    isFound = True
                
                    while True:
                        isUnique = True
                        newStudID = input("Enter new Student ID: ")
                        for studentRecords in lines:
                            record2 = studentRecords.split()
                            if len(record2) != 0:

                                if newStudID == studID or newStudID == record2[0]:
                                    print('--------------------------------------------------------')
                                    print("Student ID already exists! Please enter a unique student ID!\n")
                                    isUnique = False
                                    break
                        if isUnique:
                            break
                    newFirstName = input("Enter new firstname: ")
                    newLastName = input("Enter new lastname: ")
                    newEmail = input("Enter new email: ")

                    print("\n===| Sections |===")
                    print("[1] IT-2101")
                    print("[2] IT-2102")
                    print("[3] IT-2103")
                    print("[4] IT-2104")
                    print("[5] IT-2105")

                    select = input("\nSelect Section: ")
                    if select == "1":
                        newSection = "IT-2101"
                    elif select == "2":
                        newSection = "IT-2102"
                    elif select == "3":
                        newSection = "IT-2103" 
                    elif select == "4":
                        newSection = "IT-2104"
                    elif select == "5":
                        newSection = "IT-2105"
                    else:
                        print("\nInvalid input\nPlease try again...\n")
                        addStudent()

                    newRecord = [newStudID, newFirstName, newLastName, newEmail, newSection]                   
                    for i in range(len(newRecord)):
                        if newRecord[i] == "":
                            newRecord[i] = record[i]
                
                    student = Student(newRecord[0], newRecord[1], newRecord[2], newRecord[3], newRecord[4])
                    lines[n] = student.values().strip() + "\n"
                    break

        with open("StudentRecord.txt", "w") as fp:
            for line in lines:
                fp.write(line.lstrip())        
        fp.close

        if not isFound:
            print('--------------------------------------------------------')
            print("Student doesn't exist!\n")
        else:
            print('--------------------------------------------------------')
            print("Student Updated Successfully!\n")

def deleteStudent():
    print("\n===| DELETE STUDENT |===")
    choice = input("Search by \n[1] Lastname\n[2] Student ID #\nChoice: ")

    if choice == '1':
        lastname = input('Enter lastname: ')
        isFound = False
        count = 0
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            for studentRecords in lines:
                record = studentRecords.split()
                if len(record) != 0:
                    if lastname == record[2]:
                        count = count + 1
                        isFound = True
            if not isFound:
                print("Student doesn't exist!\n")
            elif count > 1:
                isFound = False
                studID = input("There are multiple students with the same Last Name!\nPlease enter the Student ID instead: ")
                with open("StudentRecord.txt", "w") as fp:
                    for line in lines:
                        record2 = line.split()
                        if len(record2) != 0:
                            if record2[0] != studID:
                                fp.write(line)
                            else:
                                isFound = True
                        else:
                            fp.write(line)
                if isFound:
                    print('--------------------------------------------------------')
                    print("Student Deleted Successfully!\n")
                else:
                    print('--------------------------------------------------------')
                    print("Student doesn't exist!\n")
                
                
                fp.close
            else:
                with open("StudentRecord.txt", "w") as fp:
                    for line in lines:
                        record2 = line.split()
                        if len(record2) != 0:
                            if record2[2] != lastname:
                                fp.write(line)
                        else:
                            fp.write(line)
                print('--------------------------------------------------------')
                print("Student Successfully Deleted!\n")
                fp.close
    elif choice == '2':
        studentId = input('Enter Student ID Number: ')
        isFound = False
        with open("StudentRecord.txt", "r") as fp:
            lines = fp.readlines()
            with open("StudentRecord.txt", "w") as fp:
                for line in lines:
                    record = line.split()
                    if len(record) != 0:
                        if record[0] != studentId:
                            fp.write(line)
                        else:
                            isFound = True
                    else:
                        fp.write(line)
            fp.close
            if not isFound:
                print('--------------------------------------------------------')
                print("Student doesn't exist!\n")
            else:
                print('--------------------------------------------------------')
                print("Student Successfully Deleted!\n")

def my_sort(line):
    line_fields = line.strip().split()
    id = int(line_fields[0])
    return id

def displayAll():
    print("\n===| ALL STUDENT |===")
    with open("StudentRecord.txt", "r") as fp:
        fp.readline()
        print("{:<25} {:<25} {:<25} {:<25} {:<25}".format("Student ID", "Firstname", "Lastname", "Email", "Section"))
        lines = fp.readlines()
        lines.sort(key=my_sort)
        for line in lines:
            print("{:<25} {:<25} {:<25} {:<25} {:<25}".format(line.split()[0],line.split()[1],line.split()[2],line.split()[3],line.split()[4]))
        print("")


def displaySections():
    print("\n===| STUDENT SECTIONS |===")
    with open("StudentRecord.txt", "r") as fp:
        print(f"{'Section':<22} {' Count'}")
        fp.readline()
        lines = fp.readlines()
        so = []
        tdict = {}
        for n in range(len(lines)):
         sec = lines[n].split()
         if sec[4] in tdict.keys():
          tdict.update({sec[4]: (tdict.get(sec[4])+1)})
         else:
            so.append(sec[4])
            tdict[sec[4]] = 1
         
    for k, v in tdict.items():
        print(f"{k:<25} {v}")

    print("")


# Welcome Text
print('\n===== WELCOME TO =====\nSTUDENT RECORDS SYSTEM\n')

choice = ""
while (choice != '7'):
    printMenu()
    choice = input('\nSelect your operation: ')
    if choice == '1':
        addStudent()
    elif choice == '2':
        searchStudent()
    elif choice == '3':
        editStudent()
    elif choice == '4':
        deleteStudent()
    elif choice == '5':
        displayAll()
    elif choice == '6':
        displaySections()
    elif choice == '7':
        print('\nThank You For Using Our Program!\nHave A Nice Day!\n')
    else:
        print('\nInvalid input!\nPlease Try Again!\n')
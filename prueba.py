import json 
#list
list = []


#add
def new_student():
    name = input('new student: ')

    try:
        id = float(input('ID: '))
        age = int(input('Age: '))
        course = (input('course: '))
        status = input('status: ')
    except:
        print("Error: You must enter valid numbers\n")
        return
    
    student = {
        'name': name, 
        'ID': id, 
        'age': age, 
        'program cursor': course, 
        'status': status,
        }

    list.append(student)
    print('student added successfully\n')

#cnsult
def consult_studen():
    if len(list) == 0:
        print('not found')
    else:
        print('---- student list ----')
        for p in list:
            print(f"name:{p['name']}\nID:{p['id']}\n Phone:{['age']}\n Program cursor:{p['course']}\n Status{p['status']}\n") 
        print()
    return




#save 
def save():
    if len(list) == 0:
        print("There is no data to save.\n")
        return
      
    try:
        student = open("list.json", "w", encoding="utf-8")
        json.dump(list, student, indent=4)
        student.close()
        print("Student saved in list.json\n")
    except:
        print("Error saving file\n")
    
#upload json
def upload():
    global list

    try:
        student = open("list.json", "r", encoding = "utf-8")
        list = json.load(student)
        student.close()
        print ('Student list uploaded successfully')
    except: 
        print("Error loading the list")



#menu
def menu():
    print('···· Menu ····')
    print('1.Register new students.')
    print('2.Check the student list.')
    print('3.Search for student')
    print("4. Update a student's information.")
    print('5.Remove students.')
#json
    print('6.upload json file')
    print('7.save as json')
    

def run_program():
    go_out = False
    while go_out == False:
        menu()
        break

    opcion = input("Choose an option: ")

    if opcion == "1":
        new_student()
        

    elif opcion == "2":
        consult_studen()

    elif opcion == "3":
        updated()

    elif opcion == "4":
        upload()

    elif opcion == "5":
        save()

    elif opcion == "6":
        print("Leaving the program...")
        go_out = True

    else:
        print("Invalid option, please try again\n")


run_program()



def select_department():
    print("Software Development | 1")
    print("Artificial Intelligence | 2")
    print("Research and Development | 3")
    print("Quality Assurance | 4")
    print("IT Operations | 5")
    print("Human Resources | 6")
    while True:
        try:
            choice = int(input("What is your department choice ? (1-6): "))
            if 1 <= choice <= 6:
                return choice  
            else:
                print("Invalid Choice")
        except ValueError:
            print("Invalid Choice")
            
            
def get_department_name(choice):
    if choice == 1:
        return "Software Development"
    elif choice == 2:
        return "Artificial Intelligence"
    elif choice == 3:
        return "Research and Development"
    elif choice == 4:
        return "Quality Assurance"
    elif choice == 5:
        return "IT Operations"
    elif choice == 6:
        return "Human Resources"
    return choice 

def display_employes(department):
    deptname = get_department_name(department)
    with open("employees.txt","r") as employees:
                      
        while True:
            id = employees.readline().strip()
            if id == "":
                break

            first_name = employees.readline().strip()     
            last_name = employees.readline().strip()     
            job = employees.readline().strip()            
            depart = employees.readline().strip()  
            satir6 = employees.readline() .strip()        
            employees.readline()                   

            
            if deptname == depart:
                print(f"ID: {id}")
                print(f"Name : {first_name} {last_name}")
                print(f"Title: {job}")
                print(f"Departman: {depart}")
                print("-" * 25)


def assign_weekly_tasks(department):
    deptname =get_department_name(department)
    display_employes(department)
    while True:
        description = input("Enter your task description : ")
        if description == "":
            print("Task description cannot be empty")
        else:
            break  
        
        
    while True:
        try:
            hour = int(input("Enter your estimated hours (1-40) : "))
            if hour < 1 or hour > 40:
                print("Estimated hours must be between 1 and 40")
            else:
                break 
        except ValueError:
            print("Invalid input!")
    with open(f"tasks_{department}","a") as task:
        with open("employees.txt","r") as employees:
                              
                while True:
                    id = employees.readline().strip()
                    if id == "":
                        break
        
                    first_name = employees.readline().strip()     
                    last_name = employees.readline().strip()     
                    job = employees.readline().strip()            
                    depart = employees.readline().strip()  
                    satir6 = employees.readline() .strip()        
                    employees.readline()                   
        
                    
                    if deptname == depart:
                        task.write(f"{id}\n")
                        task.write(f"{description}\n")
                        task.write(f"{hour}\n")
                        task.write("\n")
        
    
        

        
        
    

assign_weekly_tasks(select_department())
    
    
    
    
        

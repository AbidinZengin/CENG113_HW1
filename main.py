
 
def select_department():
    print("Software Development | 1")
    print("Artificial Intelligent | 2")
    print("Research and Development | 3")
    print("Quality Assurance | 4")
    print("IT Operations | 5")
    print("Human Resources | 6")
    department = ""
    
    try :
        choice = int(input("What is your department choice ? (1-6)"))
        if choice==1:
            department="Software Development"
        elif choice==2:
            department="Artificial Intelligence"
        elif choice==3:
            department="Research Development"
        elif choice==4:
            department="Quality Assurance"
        elif choice==5:
            department="IT Operations"  
        elif choice==6:
            department="Human Resources"
        else :
             print("Invalid Choice")
     
    except ValueError:
        print("Invalid Choice")
    return department , choice

def display_employes(department):
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

            
            if department == depart:
                print(f"ID: {id}")
                print(f"Name : {first_name} {last_name}")
                print(f"Title: {job}")
                print(f"Departman: {depart}")
                print("-" * 25)


display_employes(select_department())


def assign_weekly_tasks(department):
    
    print()
    
        

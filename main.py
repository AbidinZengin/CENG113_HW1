
# CENG113 HOMEWORK 1

#THIS FIELD FOR TASK 1: Display department employees
# We use select_department() for returning a number but also we use get_department_name()
# for representing choice of department and display


# This method ask user to their department turn it to a corresponding integer value
def select_department():
    print("Software Development | 1")
    print("Artificial Intelligence | 2")   # File order representation
    print("Research and Development | 3")
    print("Quality Assurance | 4")
    print("IT Operations | 5")
    print("Human Resources | 6")
    while True:
        try:      # While converting input string value to integer value errors can occur
            choice = int(input("What is your department choice ? (1-6): "))
            if 1 <= choice <= 6:     # For valid ınput
                return choice  
            else:
                print("Invalid Choice") # For invalid input
        except ValueError:     # We handle them here
            print("Invalid Choice")
    # We use while true to not interrupt the program if user enter invalid input asks until it enter valid one 
            
# This method for visual representation of each department      
def get_department_name(choice):    # Representing department only number might be confusing 
    if choice == 1:                 # So we use a helper function to handle this
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

# This method shows the selected department infos generally 
def display_employees(department):
    deptname = get_department_name(department) # For department name we use our helper function
    with open("employees.txt","r") as employees:  # Since we only read data used "r" mode 
                      
        while True:
            id = employees.readline().strip()  
            if id == "":  
                break    # Until the last line is null continue the loop
                         # Data in file generaly repetition of seperated seven lines 
                         
            first_name = employees.readline().strip()     
            last_name = employees.readline().strip()   # We catch seven lines in each loop
            job = employees.readline().strip()            
            depart = employees.readline().strip()  
            role = employees.readline() .strip()        
            employees.readline()                   

            if deptname == depart:        # Then we print all of them as intented
                print(f"ID: {id}")
                print(f"Name : {first_name} {last_name}")
                print(f"Title: {job}")
                print(f"Departman: {depart}")
                print(f"Role : {role}")
                print("-" * 25)
                



#THIS FIELD FOR TASK 2 : Assign weekly tasks 
# We generally use same methodology for accessing data, known file body means place data to correct form 0-7

# Returns True if tasks_N.txt exists and already holds at least one assignment
def tasks_exist(department):
    try:
        with open(f"tasks_{department}.txt", "r") as tasks:
            return tasks.readline().strip() != ""
    except FileNotFoundError:                   # No file yet is the expected initial condition
        return False


# This method assigns a task for  all emplooyes of a spesific department
def assign_weekly_tasks(department):
    deptname =get_department_name(department)  # Again used helper function

    # Existing assignments may be replaced only after the report was rejected
    if tasks_exist(department):
        if read_review_line(department, 1) != "Rejected":
            print("Tasks are already assigned. They can be replaced only after the report is rejected.")
            return
        answer = input("The report was rejected. Replace the existing tasks? (y/n): ").strip().lower()
        if answer != "y":
            print("No changes were made.")
            return

    with open(f"tasks_{department}.txt","w") as task: # "w" mode so each employee keeps exactly one task record
        with open("employees.txt","r") as employees:

            while True:
                id = employees.readline().strip()
                if id == "":
                    break

                first_name = employees.readline().strip()  # We never used this data just for skipping to department we want
                last_name = employees.readline().strip()   
                job = employees.readline().strip()
                depart = employees.readline().strip()
                role = employees.readline().strip()
                employees.readline()

                if deptname == depart:     # When we find matching department we write in a task file
                    print(f"ID: {id} | Name: {first_name} {last_name} | Title: {job}")

                    while True:         # Until we get valid input ask for user
                        description = input("Enter task description : ").strip()
                        if description == "":
                            print("Task description cannot be empty")
                        else:
                            break

                    while True:
                        try:    # We again have a string convertation to integer Value errors can occur
                            hour = int(input("Enter estimated hours (1-40) : "))
                            if hour < 1 or hour > 40:
                                print("Estimated hours must be between 1 and 40")
                            else:
                                break
                        except ValueError:  # We handle this errors here
                            print("Invalid input! Please enter a whole number")

                    task.write(f"{id}\n")    # Employees id , task discription and hour
                    task.write(f"{description}\n")
                    task.write(f"{hour}\n")
                    task.write("\n")



#THIS FIELD FOR TASK 3 : Generate meeting report 
# There are some helper functions here that read and write the task and review files, so other tasks can reuse them

# Returns the description num = 2 or the hours num = 3 of the employee's task
def read_task_field(department, id, num):     # Ease of reading data when we have id and department
    try:                                      # We already know the body of file so also which data placed where
        with open(f"tasks_{department}.txt", "r") as tasks:
            while True:
                task_id = tasks.readline().strip()
                if task_id == "":
                    break
                description = tasks.readline().strip()
                hours = tasks.readline().strip()    
                tasks.readline() 
                if task_id == id:   # field 2 for command description field 3 for hours
                    if num == 2:
                        return description
                    return hours
    except FileNotFoundError:
        pass
    return "" # Returns "" if the employee has no task


# Report can be generated only if every employee of the department has exactly one valid task
def tasks_are_complete(department):
    deptname = get_department_name(department)
    try:
        with open("employees.txt", "r") as employees:
            while True:                            # Again we pass thru seven lines to access dept
                id = employees.readline().strip()
                if id == "":
                    break
                employees.readline()            
                employees.readline()          
                employees.readline()            
                depart = employees.readline().strip()
                employees.readline()           
                employees.readline()            

                if depart == deptname:   # when we find the department 
                    if count_task_records(department, id) != 1: # we check for that employees task number is exactly one
                        print(f"Employee {id} does not have exactly one task. Assign tasks first.")
                        return False     # if 1 we found the right employee 
                    description = read_task_field(department, id, 2) # catch description 
                    if description == "":
                        print(f"Employee {id} has an invalid task.")
                        return False
                    try:                                             # hours must be a whole number from 1 to 40
                        hours = int(read_task_field(department, id, 3))
                    except ValueError:
                        print(f"Employee {id} has invalid estimated hours.")
                        return False
                    if hours < 1 or hours > 40:
                        print(f"Employee {id} has invalid estimated hours.")
                        return False
        return True
    except FileNotFoundError:
        print("employees.txt could not be found.")
        return False

# Returns the given line of review_N.txt
def read_review_line(department, line_number):
    try:
        with open(f"review_{department}.txt", "r") as review:
            line = ""
            for i in range(line_number):        # read lines one by one until we reach the wanted one
                line = review.readline().strip()
            return line
    except FileNotFoundError:                   # Missing review file is the expected initial condition
        return ""

# Saves the six review lines: status, reviewer id, reviewer name, comment, meeting date, meeting note
def write_review_file(department, status, reviewer_id, reviewer_name, comment, meeting_date, meeting_note):
    with open(f"review_{department}.txt", "w") as review:
        review.write(f"{status}\n")
        review.write(f"{reviewer_id}\n")
        review.write(f"{reviewer_name}\n")
        review.write(f"{comment}\n")
        review.write(f"{meeting_date}\n")
        review.write(f"{meeting_note}\n")

# Builds the meeting_report_N.txt from employees.txt and the saved tasks
def write_meeting_report(department, status, reviewer_id, reviewer_name, comment, meeting_date, meeting_note):
    deptname = get_department_name(department)
    employee_count = 0
    total_hours = 0
    with open(f"meeting_report_{department}.txt", "w") as report:  # Now we open "w" mode 
        report.write(f"Department: {deptname}\n")
        report.write(f"Meeting Date: {meeting_date}\n")
        report.write(f"Meeting Note: {meeting_note}\n")
        report.write(f"Status: {status}\n")
        report.write(f"Reviewer ID: {reviewer_id}\n")
        report.write(f"Reviewer Name: {reviewer_name}\n")
        report.write(f"Review Comment: {comment}\n")
        report.write("\nEmployee Tasks:\n")
        with open("employees.txt", "r") as employees:
            while True:
                id = employees.readline().strip()
                if id == "":
                    break
                first_name = employees.readline().strip()
                last_name = employees.readline().strip()
                title = employees.readline().strip()
                depart = employees.readline().strip()
                employees.readline()            
                employees.readline()            

                if depart == deptname:  # We found the asked dept now we can access thourough this info
                    description = read_task_field(department, id, 2)   # field 2 for description
                    hours = int(read_task_field(department, id, 3))   # field 3 for hours
                    report.write(f"{id} | {first_name} {last_name} | {title} | {description} | {hours} hours\n")
                    employee_count += 1
                    total_hours += hours
        average = total_hours / employee_count
        report.write(f"\nNumber of employees: {employee_count}\n")
        report.write(f"Total estimated hours: {total_hours}\n")
        report.write(f"Average estimated hours: {average:.2f}\n")

def generate_meeting_report(department):
    status = read_review_line(department, 1)    # "" means no report exists yet

    # An existing Pending Approval , Approved report cannot be be changed
    if status == "Pending Approval" or status == "Approved":
        print(f"A report already exists for this department Status: {status}.")
        return

    # Every employee must have exactly one valid task before a report can be built
    if not tasks_are_complete(department):
        return

    if status == "Rejected":
        # A rejected report can be regenerated from the currently saved tasks
        answer = input("The report was rejected. Regenerate it with the saved tasks? (y/n): ").lower()
        if answer != "y":
            print("No changes were made.")
            return
        meeting_date = read_review_line(department, 5)   # preserve the old date and note
        meeting_note = read_review_line(department, 6)
    else:
        
        # First time: ask for non-empty meeting date and note
        while True:
            meeting_date = input("Enter meeting date : ")
            if meeting_date == "":
                print("Meeting date cannot be empty.")
            else:
                break
        while True:
            meeting_note = input("Enter meeting note: ")
            if meeting_note == "":
                print("Meeting note cannot be empty.")
            else:
                break

    write_review_file(department, "Pending Approval", "-", "-", "-", meeting_date, meeting_note)
    write_meeting_report(department, "Pending Approval", "-", "-", "-", meeting_date, meeting_note)
    print("Meeting report generated. Status: Pending Approval")




#THIS FIELD FOR TASK 4 : Display meeting report 
# Task 4 just for displaying meeting report 
def display_meeting_report(department):
    try:
        with open(f"meeting_report_{department}.txt", "r") as report:
            line = report.readline()          # we only need to show everything in a meeting report file
            while line != "":                
                print(line,end="")
                line = report.readline()      
    except FileNotFoundError:             # again for handling non existing file error
        print("There is no report. ")
        pass

    

#THIS FIELD FOR TASK 5 : Reviewing meeting report 
# Here firstly we need to authenticate user whether is a manager or not 
# Then we can review meeting reports 


# This method is just a helper method for other tasks which uses employees full name 
def get_employee_full_name(employee_id):      # Used for reducing repetatively cases
    full_name = ""
    with open("employees.txt", "r") as employees:
        id = employees.readline().strip()
        while id != "" and full_name == "":   # stop when the file ends or the person is found
            first_name = employees.readline().strip()
            last_name = employees.readline().strip()
            employees.readline()              # title
            employees.readline()              # department
            employees.readline()              # role
            employees.readline()              #blank line
            if (id==employee_id):
                full_name =first_name+" "+last_name
            id = employees.readline().strip()
    return full_name


#This method verify whether specified id , password and department is matched for employee's role department and password file datas.
def authenticate_manager(manager_id, password, department):
    deptname = get_department_name(department)
    is_dept_manager = False
    try: 
        with open("employees.txt", "r") as employees:
            id = employees.readline().strip()
            while id != "" and not is_dept_manager:   # we check condition extra after finding manager it means loop ends here.
                employees.readline()          # first name
                employees.readline()          # last name
                employees.readline()          # title
                depart = employees.readline().strip()
                role = employees.readline().strip()
                employees.readline()          # blank line
                if(id==manager_id and role=="Manager" and depart==deptname): # we catch here intented conditions 
                    is_dept_manager=True                                     # where role is manager for asked id employee
             
                id = employees.readline().strip()    #next employee id we have to  get this 
    
    except FileNotFoundError:     
        print("employees.txt could not be found.")
        return False

    if not is_dept_manager:    # Now we found the manager role and department is matched for asked id 
        return False           # We need to verify for password now

    password_ok = False
    try:
        with open("manager_passwords.txt", "r") as passwords:
            saved_id = passwords.readline().strip()        
            while saved_id != "" and not password_ok:    # we only access id and password iteratively 
                saved_password = passwords.readline().strip()
                passwords.readline()          # blank line
                if (saved_id == manager_id and saved_password==password): 
                     password_ok=True
                saved_id = passwords.readline().strip()
    except FileNotFoundError:
        print("manager_passwords.txt could not be found.")
        return False

    return password_ok

# Lets a manager of the department approve or reject a "Pending Approval" meeting report after login.
def review_meeting_report(department):
    status = read_review_line(department, 1)   #check current status first
    if status=="" :
        print("There is no report.")   
        return
    if (status!="Pending Approval"):               # Only reports with the status Pending Approval can be reviewed
            print(f"This report is already {status}.")
            return

    attempts = 0  # Only at most three attempts for login
    logged_in = False
    while attempts < 3 and not logged_in:
        manager_id = input("Enter Manager ID: ")  # Get manager id and pwassword from user
        password = input("Enter Password: ")      
        if authenticate_manager(manager_id, password, department):
            logged_in = True
        else:
            print("Invalid manager ID or password, or unauthorized department.")
        attempts += 1

    if not logged_in:
        return                                # 3 failed attempts means back to menu 

    display_meeting_report(department)        # show the report after login

    #what do you want to do with this report
    decision = ""
    while decision != "1" and decision != "2" and decision != "3":
        decision = input("1. Approve  2. Reject  3. Cancel: ").strip()

    if decision == "3":                    #if review meeting cancel it will occur
        print("Review cancelled. No changes were made.")   
        return

    if decision == "1":
            new_status = "Approved"
            comment = input("Approval comment (optional): ").strip()
            if comment == "":
                comment = "-"
    else:
            new_status = "Rejected"
            comment = input("Rejection comment: ").strip()
            while comment == "":                  
                print("Rejection comment cannot be empty.")  #We have give rejection comment
                comment = input("Rejection comment: ").strip()


    reviewer_name = get_employee_full_name(manager_id)       #we already define a helper funtion to this request
    meeting_date = read_review_line(department, 5)   #meeting date on the 5. line on the review report
    meeting_note = read_review_line(department, 6)  #meeting date meeting note on the 6. line on the review report
    write_review_file(department, new_status, manager_id, reviewer_name, comment, meeting_date, meeting_note)  #write func hast hese parameters check
    write_meeting_report(department, new_status, manager_id, reviewer_name, comment, meeting_date, meeting_note) #report has same columns
    print(f"Report {new_status}.")




#THIS FIELD FOR TASK 6 : Displaying Task Summary 
# Counts how many task records in tasks_n.txt belong to this employee id
def count_task_records(department, id):
    count = 0           # task files has four repetative lines 
    try:
        with open(f"tasks_{department}.txt", "r") as tasks:
            while True:  # task files has four repetative lines
                task_id = tasks.readline().strip()  
                if task_id == "":              # we access data thru 4 lines
                    break                       
                tasks.readline()                # description
                tasks.readline()                # hours
                tasks.readline()                
                if task_id == id:
                    count += 1 
    except FileNotFoundError:                   # No tasks saved yet, so count stays 0
        pass
    return count

# This method isplays the department employee count, number of assigned tasks, total estimated hours and average hours per assigned task.
def display_task_summary(department):
    deptname = get_department_name(department)
    employee_count = 0
    task_count = 0
    total_hours = 0
    try:
        with open("employees.txt", "r") as employees: 
            id = employees.readline().strip()
            while id != "":
                employees.readline()
                employees.readline()
                employees.readline()
                depart = employees.readline().strip()
                employees.readline()
                employees.readline()
                if depart == deptname:
                    employee_count += 1  
                    if count_task_records(department, id) > 0:   # we already have helper method to count tasks 
                        task_count += 1
                        total_hours += int(read_task_field(department, id, 3))  # result of function already a number 
                id = employees.readline().strip()                               # so we do not need to handle value converting error
    except FileNotFoundError:
        print("employees.txt could not be found.")
        return

    print(f"Department: {deptname}")                
    print(f"Number of employes: {employee_count}")
    print(f"Assigned tasks: {task_count}")
    print(f"Total estimated hours: {total_hours}")
    if task_count == 0:
        print("Average hours per task: N/A")
    else:
        print(f"Average hours per task: {total_hours / task_count:.2f}")  #formatted




#THIS FIELD FOR THE MAIN MENU
# Displays the main menu
def display_menu():                            
    print("\n1. Display department employees")
    print("2. Assign weekly tasks")
    print("3. Generate meeting report")
    print("4. Display meeting report")
    print("5. Review meeting report")
    print("6. Display task summary")
    print("0. Exit")


# Runs the menu loop and calls the other functions
def main():
    while True:         # Menu is shown again after every option until the user selects 0
        display_menu()
        try:            # Converting input to integer can raise ValueError
            choice = int(input("Enter your choice: "))
            print()
        except ValueError:
            print("Invalid Choice")
            continue

        if choice == 0:
            print("Program has ended!")
            break
        elif choice == 1:
            display_employees(select_department())
        elif choice == 2:
            assign_weekly_tasks(select_department())
        elif choice == 3:
            generate_meeting_report(select_department())
        elif choice ==4:
            display_meeting_report(select_department())
        elif choice ==5:
            review_meeting_report(select_department())
        elif choice == 6:
            display_task_summary(select_department())

main()

    
    
    
    


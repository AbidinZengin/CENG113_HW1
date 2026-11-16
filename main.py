
# CENG113 HOMEWORK 1

#----------------------------------------------------------------------#
#THIS FIELD FOR TASK 1: Display department employees
#----------------------------------------------------------------------#
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
            last_name = employees.readline().strip()   # We catch seven lines each loop
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
                
#----------------------------------------------------------------------#



#----------------------------------------------------------------------#
#THIS FIELD FOR TASK 2 : Assign weekly tasks 
#----------------------------------------------------------------------#

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

                first_name = employees.readline().strip() # We never used this data just for skipping to department
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
#----------------------------------------------------------------------#



#----------------------------------------------------------------------#
#THIS FIELD FOR TASK 3 : Generate meeting report 
#----------------------------------------------------------------------#
 
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


# Returns the description (field 2) or the hours (field 3) of the employee's task
def read_task_field(department, id, field):     # Ease of reading data when we have id and dept 
    try:
        with open(f"tasks_{department}.txt", "r") as tasks:
            while True:
                task_id = tasks.readline().strip()
                if task_id == "":
                    break
                description = tasks.readline().strip()
                hours = tasks.readline().strip()    
                tasks.readline() 
                if task_id == id:   # field 2 for command description field 3 for hours
                    if field == 2:
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

#----------------------------------------------------------------------#
#THIS FIELD FOR THE MAIN MENU
#----------------------------------------------------------------------#

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
        except ValueError:
            print("Invalid Choice")
            continue

        if choice == 0:
            print("Goodbye")
            break
        elif choice == 1:
            display_employees(select_department())
        elif choice == 2:
            assign_weekly_tasks(select_department())
        elif choice == 3:
            generate_meeting_report(select_department())
        elif choice == 4:
            display_meeting_report(select_department())
        elif choice == 5:
            review_meeting_report(select_department())
        elif choice == 6:
            display_task_summary(select_department())
        else:
            print("Invalid Choice")


def display_meeting_report(department):
    try:
        with open(f"meeting_report_{department}.txt", "r") as f:
            while True:
                line = f.readline()
                if line == "":
                    break
                else:
                    print(line, end="")
    except FileNotFoundError:
        print("No meeting report found for this department.")
        return


def authenticate_manager(manager_id, password, department):
    deptname = get_department_name(department)
    try:
        with open("employees.txt", "r") as f:
            while True:
                employee_id = f.readline().strip()
                if employee_id == "":
                    break

                f.readline()
                f.readline()
                f.readline()
                depart = f.readline().strip()
                role = f.readline().strip()
                f.readline()

                if employee_id == str(manager_id) and depart == deptname and role == "Manager":
                    try:
                        with open("manager_passwords.txt", "r") as file:
                            while True:
                                id_check = file.readline().strip()
                                if id_check == "":
                                    break
                                password_check = file.readline().strip()
                                file.readline()

                                if id_check == employee_id and password_check == password:
                                    return True

                    except FileNotFoundError:
                        print("Manager passwords file not found")
                        return False
                    break
    except FileNotFoundError:
        print("Employees file not found.")
        return False

    return False


def review_meeting_report(department):
    global manager_id
    attempts = 0

    try:
        with open(f"meeting_report_{department}.txt", "r") as f:
            pass
    except FileNotFoundError:
        print("No meeting report found.")
        return

    status = read_review_line(department, 1)
    if status == "Approved" or status == "Rejected":
        print(status)
        return

    if status != "Pending Approval":
        print("Invalid or missing report status.")
        return

    login_successful = False

    while attempts < 3:
        attempts += 1

        manager_id = input("Please write your employee ID: ")
        password = input("Please write your Manager password: ")
        if authenticate_manager(manager_id, password, department) == True:
            print("Login successful.")
            login_successful = True
            break
        else:
            print("Invalid manager ID or password, or unauthorized department.")

    if attempts == 3 and login_successful == False:
        print("Max attempts reached.")
        return

    display_meeting_report(department)

    while True:
        print("1. Approve")
        print("2. Reject")
        print("3. Cancel")
        choice = input("Enter your choice:")

        if choice == "1":
            status = "Approved"
            comment = input("Please write your comment: ").strip()
            if comment == "":
                comment = "-"
            break
        elif choice == "2":
            status = "Rejected"
            while True:
                comment = input("Please write your comment: ").strip()
                if comment == "":
                    print("Rejection comment cannot be empty.")
                else:
                    break
            break
        elif choice == "3":
            return

        else:
            print("Invalid choice.")

    try:
        with open("employees.txt", "r") as f:
            while True:
                employee_id = f.readline().strip()
                if employee_id == "":
                    break

                first_name = f.readline().strip()
                last_name = f.readline().strip()
                f.readline()
                f.readline()
                f.readline()
                f.readline()

                if manager_id == employee_id:
                    reviewer_name = first_name + " " + last_name
                    break
    except FileNotFoundError:
        print("Employees file not found.")
        return

    meeting_date = read_review_line(department, 5)
    meeting_note = read_review_line(department, 6)

    write_review_file(department, status, manager_id, reviewer_name, comment, meeting_date, meeting_note)
    write_meeting_report(department, status, manager_id, reviewer_name, comment, meeting_date, meeting_note)
    print(f"Report status: {status}.")


def display_task_summary(department):
    deptname = get_department_name(department)
    employee_count = 0
    task_count = 0
    total_hours = 0
    try:
        with open("employees.txt", "r") as f:
            while True:
                id = f.readline().strip()
                if id == "":
                    break

                f.readline()
                f.readline()
                f.readline()
                depart = f.readline().strip()
                f.readline()
                f.readline()

                if deptname == depart:
                    employee_count += 1
    except FileNotFoundError:
        print("Employees file not found.")
        return

    try:
        with open(f"tasks_{department}.txt", "r") as f:
            while True:
                id = f.readline().strip()
                if id == "":
                    break
                f.readline()
                time = f.readline().strip()
                f.readline()
                task_count += 1
                total_hours += int(time)
    except FileNotFoundError:
        print("No tasks  found for this department.")

    if task_count > 0:
        average = f"{total_hours / task_count:.2f}"
    else:
        average = "N/A"

    print(f"Department: {deptname}\nNumber of employees: {employee_count}\nNumber of assigned tasks: {task_count}\nTotal estimated hours: {total_hours}\nAverage hours per task:{average}")




main()


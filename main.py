import mysql.connector
from admin.sql_commands import sqlCommands
from admin.sql_file import sqlFile
from employee.manipulate import manipulate
from operations.view import viewIntermediate, viewBeginner

def loginUser():
    user = input("Please enter username:")
    password = input("Please enter password: ")
    host = input("Please enter server host: ")
    port = int(input("Please enter port number: "))
    database = "museum"

    ## DEBUG
    # user = "root"
    # password = "appleseed"
    # host = "localhost"
    # port = 3306
    # database = "museum"

    cnx = mysql.connector.connect(
        host= host,
        port= port,
        user= user,
        password= password,
        database= database,
    )
    return cnx


def adminMenu(cnx, cur):

    print("Welcome to the Admin Interface.\
          \nHere you can directly edit the database through SQL commands")
    while True:
        # Main idea is to give the admin an interface to type any command they wish
        print("Please select what operation you would like to perform\
            \n1. SQL Commands\n2. SQL file")
        
        while True:
            try:
                choice = int(input("Please enter 1 or 2:  "))
                if choice < 1 or choice > 2:
                    print("\nInvalid input. Please enter 1 or 2")
                    input("<<Press Enter to continue>>\n\n")
                    continue
                break
            except Exception:
                print("\nInvalid input. Please enter 1 or 2")
                input("<<Press Enter to continue>>\n\n")
                continue

        if choice == 1:
            sqlCommands(cnx, cur)
        elif choice == 2:
            sqlFile(cnx, cur)
        
        while True:
            try:
                choice = input("Would you like to perform another operation? yes/no: ").lower()
                if choice not in ['yes', 'y', 'no', 'n']:
                    print("\nInvalid input. Please enter yes or no")
                    input("<<Press Enter to continue>>\n\n")
                    continue
                break
            except Exception:
                print("\nInvalid input. Please enter yes or no")
                input("<<Press Enter to continue>>\n\n")
                continue

        if choice.lower() in ['yes', 'y']: 
            continue
        elif choice.lower() in ['n', 'no']: 
            print("Thank you")
            break
    return

def employeeMenu(cnx, cur):

    print("Welcome to the employee Interface\n")
    while True:
        print("What operation would you like to perform\
              \n1. View\n2. Manipulate")
        
        while True:
            try:
                choice = int(input("Please enter 1 or 2: "))
                if choice < 1 or choice > 2:
                    print("\nInvalid input. Please enter 1 or 2")
                    input("<<Press Enter to continue>>\n\n")
                    continue
                break
            except Exception:
                print("\nInvalid input. Please enter 1 or 2")
                input("<<Press Enter to continue>>\n\n")
                continue

        if choice == 1:
            print("We offer two viewing experiences.\
                  \nThe first one is designed for users who fairly know what they're doing\
                  \nThe second one is designed for first timers.\
                  \nPlease choose one of the two experiences.\
                  \n1. Intermidiate\n2. Beginner")
            
            while True:
                try:
                    experience_choice = int(input("Please enter a number 1 or 2:  "))
                    if experience_choice < 1 or experience_choice > 2:
                        print("\nInvalid input. Please enter 1 or 2")
                        input("<<Press Enter to continue>>\n\n")
                        continue
                    break
                except Exception:
                    print("\nInvalid input. Please enter 1 or 2")
                    input("<<Press Enter to continue>>\n\n")
                    continue

            if experience_choice == 1: viewIntermediate(cnx, cur)
            elif experience_choice == 2: viewBeginner(cnx, cur)

        elif choice == 2:
            manipulate(cnx, cur)

        while True:
            try:
                choice = input("Would you like to perform another operation? yes/no: ").lower()
                if choice not in ['yes', 'y', 'no', 'n']:
                    print("\nInvalid input. Please enter yes or no")
                    input("<<Press Enter to continue>>\n\n")
                    continue
                break
            except Exception:
                print("\nInvalid input. Please enter yes or no")
                input("<<Press Enter to continue>>\n\n")
                continue

        if choice.lower() in ['yes', 'y']: 
            continue
        elif choice.lower() in ['n', 'no']: 
            print("Thank you")
            break
    return

def guestMenu(cnx, cur):

    print("Welcome to the guest Interface\n")
    while True:
        print("We offer two viewing experiences.\
        \nThe first one is designed for users who fairly know what they're doing\
        \nThe second one is designed for first timers.\
        \nPlease choose one of the two experiences.\
        \n1. Intermidiate\n2. Beginner")

        while True:
            try:
                experience_choice = int(input("Please enter a number 1 or 2:  "))
                if experience_choice < 1 or experience_choice > 2:
                    print("\nInvalid input. Please enter 1 or 2")
                    input("<<Press Enter to continue>>\n\n")
                    continue
                break
            except Exception:
                print("\nInvalid input. Please enter 1 or 2")
                input("<<Press Enter to continue>>\n\n")
                continue


        if experience_choice == 1: viewIntermediate(cnx, cur)
        elif experience_choice == 2: viewBeginner(cnx, cur)


        while True:
            try:
                choice = input("Would you like to perform another operation? yes/no: ").lower()
                if choice not in ['yes', 'y', 'no', 'n']:
                    print("\nInvalid input. Please enter yes or no")
                    input("<<Press Enter to continue>>\n\n")
                    continue
                break
            except Exception:
                print("\nInvalid input. Please enter yes or no")
                input("<<Press Enter to continue>>\n\n")
                continue

        if choice.lower() in ['yes', 'y']: 
            continue
        elif choice.lower() in ['n', 'no']: 
            print("Thank you")
            break

    return

if __name__ == "__main__": # BIG REMINDER TO TRY EXCEPT THE EXECUTE FUNCTIONS 
    cnx = loginUser()
    cur = cnx.cursor()

    # run create.sql
    print("Creating database...")
    fd = open('create.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cur.execute(command)
        except IOError as e:
            print("Command skipped: ",e)

    print("Database created successfully\n")

    # main code
    print("Welcome to the Museum Database")

    while True:
        try:
            choice = int(input("Are you a/an\n1. Admin\n2. Employee\n3. Guest\nOr enter 4 to quit.\
                               \n\nPlease enter 1, 2, 3 or 4:  "))
            if choice < 1 or choice > 4:
                print("Invalid input. Please enter a number between 1 and 4")
                input("<<Press Enter to continue>>\n\n")
                continue
            break
        except Exception:
            print("Invalid input. Please enter a number betweeen 1 and 4")
            input("<<Press Enter to continue>>\n\n")
            continue

    if choice == 1:
        adminMenu(cnx, cur)
    elif choice == 2:
        employeeMenu(cnx, cur)
    elif choice == 3:
        guestMenu(cnx, cur)
        
    print("Thank you for using the Museum Database. Goodbye.")

    cnx.close()
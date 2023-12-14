from operations.display import displayResult

def sqlCommands(cnx, cur):

    while True:
        try:
            choice = int(input("\nPlease choose which operation you want to perform.\
                                \n1. Insert, Update or Delete (Manipulation)\n2. Select (View)\n3. Other\
                               \nPlease type 1, 2 or 3:   "))
            if choice < 1 or choice > 3:
                print("\nInvalid input. Please enter 1, 2 or 3")
                input("<<Press Enter to continue>>\n\n")
                continue
            break
        except Exception:
            print("\nInvalid input. Please enter 1, 2 or 3")
            input("<<Press Enter to continue>>\n\n")
            continue
    
    command = input("Please enter you SQL command:\n")


    while True:
        try:
            cur.execute(command)
            if choice == 1:
                cnx.commit()
            else:
                displayResult(cur)
            break
        except Exception as e:
            print("\nSorry, it seems like there was an error with your command.")
            print(e)
            input("<<Press Enter to continue>>\n\n")
            break


    return
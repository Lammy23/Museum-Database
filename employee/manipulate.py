from operations.insert import insert
from operations.delete import delete
from operations.update import update

def manipulate(cnx, cur):
    print("What operation would you like to complete\
          \n1. Insert\n2. Delete\n3. Update")

    while True:
        try:
            choice = int(input("Please enter 1, 2 or 3: "))
            if choice < 1 or choice > 3:
                print("\nInvalid input. Please enter 1, 2 or 3")
                input("<<Press Enter to continue>>\n\n")
                continue
            break
        except Exception:
            print("\nInvalid input. Please enter 1, 2 or 3")
            input("<<Press Enter to continue>>\n\n")
            continue

    if choice == 1:
        insert(cnx, cur)
    elif choice == 2:
        delete(cnx, cur)
    elif choice == 3:
        update(cnx, cur)

    return
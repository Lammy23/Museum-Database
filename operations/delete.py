from operations.display import displayResult

def delete(cnx, cur): # code works but I can't delete from art_object because I don't have the triggers
    
    print("Which table would you like to delete from?")

    # Show all the tables
    cur.execute("SHOW TABLES")
    tables = cur.fetchall()
    clause = []

    for index, table in enumerate(tables):
        print(f"{index + 1}. {table[0]}")
    
    while True:
        try:
            choice = int(input("\nPlease enter a number: "))
            if choice < 1 or choice > len(tables):
                print("\nInvalid input. Please enter a number")
                input("<<Press Enter to continue>>\n\n")
                continue
            break
        except Exception:
            print("\nInvalid input. Please enter a number")
            input("<<Press Enter to continue>>\n\n")
            continue

    # Set the table variable
    table = tables[choice - 1][0]
    insert = f"DELETE FROM {table} WHERE "

    print(f"Here are the attributes for {table}.\nPlease indicate the criteria for deletion.")
    cur.execute(f"DESCRIBE {table}")
    attributes = cur.fetchall()

    for index, attribute in enumerate(attributes):
        print(f"{index + 1}. {attribute[0]}")
        value = input(f"Please enter the value for {attribute[0]} or press enter to skip: ") or None
        if value is None:   continue
        insert += attribute[0] + " = %s AND "
        clause.append(value)

    # Avoid errors
    clause.append(True)
    insert += " %s"

    ## DEBUG
    # print(insert)
    # print(clause)

    while True:
        try:
            cur.execute(insert, clause)
            cnx.commit()
            break
        except Exception as e:
            print("\nSorry, we ran into an error while executing your command.")
            print(e)
            input("<<Press Enter to continue>>\n\n")
            break
    return
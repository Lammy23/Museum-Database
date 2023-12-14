from operations.display import displayResult

def insert(cnx, cur):

    print("What table would you like to insert into: ")

    # Show all the tables
    cur.execute("SHOW TABLES")
    tables = cur.fetchall()

    clause = []

    for index, table in enumerate(tables):
        print(f"{index + 1}. {table[0]}")

    while True:
        try:
            choice = int(input("Please enter a number: "))
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
    insert = f"INSERT INTO {table} VALUES ("

    # Show all the attributes
    cur.execute(f"DESCRIBE {table}")
    attributes = cur.fetchall()
    
    for index, attribute in enumerate(attributes):
        # Check for null
        if attribute[2] == "NO": print("This attribute cannot be null")
        if attribute[3] == "PRI": print("This is the primary key")

        data_type = attribute[1].decode()

        print(f"Data type: {data_type}")

        print(f"{index + 1}. {attribute[0]}")
        value = input(f"Please enter the value for {attribute[0]} or press enter for null: ") or None
        if attribute == attributes[-1]: 
            insert += "%s"
        else:
            insert += "%s" + ","
        clause.append(value)
        print()

    insert += ")"

    ## DEBUG
    # print(insert)

    while True:
        try:
            cur.execute(insert, clause)
            cnx.commit()
            break
        except Exception as e:
            print("\nSorry, we ran into an error while inserting your data.")
            print(e)
            input("<<Press Enter to continue>>\n\n")
            break
    return
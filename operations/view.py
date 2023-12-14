from operations.display import displayResult
from operations.remove_comma import remove_trailing_commas

def viewIntermediate(cnx, cur):
    print("What table would you like to view:")

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
                print("\nInvalid input. Please enter a valid number")
                input("<<Press Enter to continue>>\n\n")
                continue
            break
        except Exception:
            print("\nInvalid input. Please enter a valid number")
            input("<<Press Enter to continue>>\n\n")
            continue

    # Set the table variable
    table = tables[choice - 1][0]
    insert = f"SELECT * FROM {table} WHERE "

    print(f"Here are the attributes for {table}:")
    cur.execute(f"DESCRIBE {table}")
    attributes = cur.fetchall()

    for index, attribute in enumerate(attributes):
        print(f"{index + 1}. {attribute[0]}")

        value = input(f"Please enter the value for {attribute[0]} or press enter to skip: ") or None
        if value is None:   continue
        insert += attribute[0] + " = %s AND "
        clause.append(value)

    clause.append(True) # This is to avoid errors with the AND at the end of the insert statement
    insert += " %s"

    # Debug Lines
    # print(insert)
    # print(clause)

    while True:
        try:
            cur.execute(insert, clause)
            displayResult(cur)
            break
        except Exception as e:
            print("\nSorry, we couldn't find any results matching your query.")
            print(e)
            input("<<Press Enter to continue>>\n\n")
            break
    return


def viewBeginner(cnx, cur):
    print("What information would you like to view:\
          \n1. Art objects\n2. Artists\n")

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
        viewArtObjects(cnx, cur)
    elif choice == 2:
        viewArtists(cnx, cur)
    return

def viewArtObjects(cnx, cur):
    
    print("\nThis museum has four main categories of art objects:\n1. Paintings\n2. Sculptures\
          \n3. Statues \n4. Other\n5. Everything\n")
    
    while True:
        try:
            choice = int(input("Please enter a number between 1 and 5 (Select 5 for all categories):   "))
            if choice < 1 or choice > 5:
                print("\nInvalid input. Please enter a valid number")
                input("<<Press Enter to continue>>\n\n")
                continue
            break
        except Exception:
            print("\nInvalid input. Please enter a valid number")
            input("<<Press Enter to continue>>\n\n")
            continue

    choices = {
        1: 'PAINTING',
        2: 'SCULPTURE',
        3: 'STATUE',
        4: 'OTHER',
        5: 'ART_OBJECT'
    }

    big_choice = choices[choice]

    params = []

    is_division = 1 <= choice <= 4

    if choice != 4:
        print(f"Our museum is proud of our lush category of {big_choice.lower()}s.\
            \nTo help us know which {big_choice.lower()} you would like please answer the following questions.\
            \n")
    else:
        print(f"Our museum is proud of our lush category of antique items.\
        \nTo help us know which {big_choice.lower()} you would like please answer the following questions.\
        \n")

    artist_name = False

    while True:
        try: 
            choice = input("Do you know the artist of this work?\nyes/no:  ")
            if choice.lower() not in ['yes', 'y', 'no', 'n']:
                print("\nInvalid input. Please enter yes or no")
                input("<<Press Enter to continue>>\n\n")
                continue
            break
        except Exception:
            print("\nInvalid input. Please enter yes or no")
            input("<<Press Enter to continue>>\n\n")
            continue

    if choice.lower() in ['y', 'yes']:
        artist_name = input("Please enter the artist's full name:\n")

    select_clause = "SELECT "

    if is_division:
        from_clause = f"FROM (ART_OBJECT NATURAL JOIN {big_choice}) "
        if artist_name:
            from_clause = f"FROM (ART_OBJECT AS art JOIN ARTIST AS artsy USING (id_no)) NATURAL JOIN {big_choice} "
    else:
        from_clause = f"FROM {big_choice}"
        if artist_name:
            from_clause = f"FROM (ART_OBJECT AS art JOIN ARTIST AS artsy USING (id_no))"
    where_clause = "WHERE "
    if artist_name:
        where_clause += "artist_name = %s AND "
        params.append(artist_name)

    cur.execute("DESCRIBE ART_OBJECT")
    attributes = cur.fetchall()

    for attribute in attributes:
        choice = input(f"Do you know the {attribute[0]} of the {big_choice.lower()} you would like to view?\ny/n (Press Enter to skip attribute entirely):  ") or None

        if not choice: continue

        if choice.lower() in ['y', 'yes']:
            value = input(f"Please enter the value for {attribute[0]}:\n") or None
            where_clause += attribute[0] + " = %s AND "
            params.append(value)

        while True:
            try: 
                choice = input(f"Would you like to view the {attribute[0]} of this {big_choice.lower()}?\ny/n:  ")
                if choice.lower() not in ['yes', 'y', 'no', 'n']:
                    print("\nInvalid input. Please enter yes or no")
                    input("<<Press Enter to continue>>\n\n")
                    continue
                break
            except Exception:
                print("\nInvalid input. Please enter yes or no")
                input("<<Press Enter to continue>>\n\n")
                continue

        if choice.lower() in ['y', 'yes']: select_clause += attribute[0] + ','

    where_clause += '%s'
    params.append(True)

    if is_division:
        cur.execute(f"DESCRIBE {big_choice}")
        field_attributes = cur.fetchall()

        print(f"Do you want to view specific info about the {big_choice.lower()} including {field_attributes[1][0]}, {field_attributes[2][0]} and more?")
        
        while True:
            try: 
                choice = input("y/n:  ")
                if choice.lower() not in ['yes', 'y', 'no', 'n']:
                    print("\nInvalid input. Please enter yes or no")
                    input("<<Press Enter to continue>>\n\n")
                    continue
                break
            except Exception:
                print("\nInvalid input. Please enter yes or no")
                input("<<Press Enter to continue>>\n\n")
                continue

        if choice in ['y', 'yes']:
            for attribute in field_attributes:
                select_clause += attribute[0] + ','
        
    print("Would you like to display the artist's name?")

    while True:
        try: 
            choice = input("y/n:  ")
            if choice.lower() not in ['yes', 'y', 'no', 'n']:
                print("\nInvalid input. Please enter yes or no")
                input("<<Press Enter to continue>>\n\n")
                continue
            break
        except Exception:
            print("\nInvalid input. Please enter yes or no")
            input("<<Press Enter to continue>>\n\n")
            continue

    if choice.lower() in ['y', 'yes']:
        select_clause += 'artist_name,'

    while True:
        try: 
            choice = int(input(f"Regarding the {big_choice}, would you like to see exhibition OR collection names?\
                               \n1. Collector\n2. Exhibition\n3. Neither\nPlease enter a number between 1 and 3 (Enter 3 to skip):  "))
            if choice < 1 or choice > 3:
                print("\nInvalid input. Please enter a valid number")
                input("<<Press Enter to continue>>\n\n")
                continue
            break
        except Exception:
            print("\nInvalid input. Please enter a valid number")
            input("<<Press Enter to continue>>\n\n")
            continue

    collection_or_exhibition = {
        1: 'COLLECTIONS',
        2: 'EXHIBITIONS'
    }

    if choice != 3:
        collection_or_exhibition_choice = collection_or_exhibition[choice]
        from_clause += f"NATURAL JOIN {collection_or_exhibition_choice} "
        select_clause += f"{collection_or_exhibition_choice[:-1].lower()}_name,"

    select_clause = remove_trailing_commas(select_clause)
    
    full_clause = select_clause + ' ' + from_clause + ' ' + where_clause

    ## Debug Lines
    # print(full_clause)
    # print(params)

    while True:
        try:
            cur.execute(full_clause, params)
            print("Here are the results of your query:")
            displayResult(cur)
            break
        except Exception as e:
            print("\nSorry, we ran into an error while executing your query.")
            print(e)
            input("<<Press Enter to continue>>\n\n")
            break
    return



def viewArtists(cnx, cur):
    print("Please answer the following questions to help us find the artist you are looking for.\n")

    cur.execute("DESCRIBE ARTIST")
    attributes = cur.fetchall()

    select_clause = "SELECT DISTINCT "
    from_clause =   "FROM ARTIST "
    where_clause =  "WHERE "

    params = []

    for attribute in attributes:
        choice = input(f"Do you know the {attribute[0]} of the artist you would like to view?\
                        \ny/n (Press Enter to skip attribute entirely):  ") or None

        if not choice: continue
        if choice.lower() in ['y', 'yes']:
            value = input(f"Please enter the value for {attribute[0]}:\n") or None
            where_clause += attribute[0] + " = %s AND "
            params.append(value)

        while True:
            try: 
                choice = input(f"Would you like to view the {attribute[0]} of this artist?\ny/n:  ")
                if choice.lower() not in ['yes', 'y', 'no', 'n']:
                    print("\nInvalid input. Please enter yes or no")
                    input("<<Press Enter to continue>>\n\n")
                    continue
                break
            except Exception:
                print("\nInvalid input. Please enter yes or no")
                input("<<Press Enter to continue>>\n\n")
                continue

        if choice.lower() in ['y', 'yes']: select_clause += attribute[0] + ','

    where_clause += '%s'
    params.append(True)

    select_clause = remove_trailing_commas(select_clause)

    full_clause = select_clause + ' ' + from_clause + ' ' + where_clause

    ## Debug Lines
    # print(full_clause)
    # print(params)

    while True:
        try:
            cur.execute(full_clause, params)
            print("Here are the results of your query:")
            displayResult(cur)
            break
        except Exception as e:
            print("\nSorry, we ran into an error while executing your query.")
            print(e)
            input("<<Press Enter to continue>>\n\n")
            break
    
    return
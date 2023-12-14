def displayResult(cur): # Need to work on this function

    # rows = cur.fetchall()
    # print(rows)
    col_names = cur.column_names
    search_results = cur.fetchall()
    print("Search found ", len(search_results), " results")
    header_size = len(col_names)
    for i in range(header_size):
        print("{:<15}".format(col_names[i]), end = '')
    print()
    print(15*header_size*"-") # Print a line of dashes
    for row in search_results:
        for val in row:
            print("{:<15}".format(str(val)), end= '')
        print()
    return
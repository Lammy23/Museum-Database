from operations.display import displayResult

def sqlFile(cnx, cur):

    filename = input("Please enter the name of the file you wish to execute: ")

    while True:
        try:
            cur.execute('source ' + filename)
            break
        except Exception as e:
            print("\nSorry, we ran into an error while executing your file.")
            print(e)
            input("<<Press Enter to continue>>\n\n")
            break
    displayResult(cur)

    return
# ----------------------- #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a Python dictionary.
#              Add each dictionary "row" to a Python list "table"
# ChangeLog (Who,When,What):
# EDurfey, 5/11/2021, Added code in order to complete assignment
# ----------------------- #

# Data #
# Declare variables and constants
objFileName = "ToDoFile.txt"
strData = ""
dicRow = {}
lstTable = []
strChoice = ""

# Processing #
# Step 1 - When the program starts, load from ToDoFile.txt into a Python dictionary
objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# Input/Output#
# Step 2 - Display a menu of choices to the user
while True:
    print("""
              Menu of Options
                1. Show current data
                2. Add a new item
                3. Remove an existing item
                4. Save data to a file
                5. Exit program
                """)
    strChoice = str(input("Which option would you like to perform [1 to 4]? "))
    print()
# Step 3 - Show the current item in the table
    if strChoice.strip() == '1':
        print("******* The current items to do are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue
# Step 4 - Add a new item to the list/table
    elif strChoice.strip() == '2':
        strTask = str(input("What is the task?")).strip()
        strPriority = str(input("What is the priority [high|low]?")).strip()
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        print("Current data in table:")
        print("******* The current items to do are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue
# Step 5 - Remove the new item from the list/table
    elif strChoice == "3":
        strKeyToRemove = input("Which task would you like removed?")
        blnItemRemoved = False
        intRowNumber = 0
        for row in lstTable:
            task, priority = dict(row).values()
            if task == strKeyToRemove:
                del lstTable[intRowNumber]
                blnItemRemoved = True
            intRowNumber += 1
            if blnItemRemoved = True:
                print("The task was removed.")
            else:
                print("I'm sorry, but the task could not be found.")
            print("******* The current items to do are: *******")
            for row in lstTable:
                print(row["Task"] + "(" + row["Priority"] + ")")
            print("*******************************************")
        continue
# Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == "4":
        print("******* The current items to do are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        if "y" == str(input("Save this data to file (Y/N)? ")).strip().lower():
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                print(row["Task"] + "(" + row["Priority"] + ")")
            print("*******************************************")
            if "y" == str(input("Save this data to the file (Y/N)? ")).strip().lower():
                objFile = open(objFileName, "w")
                for dicRow in lstTable:
                    objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
                objFile.close()
                input("Data saved to file! Press the [Enter] key to return to menu.")
            else:
                input("New data was NOT Saved, but previous data still exists. Press "
                      "the [Enter] key to return to menu.")
            continue
# Step 7 - Exit the program
        elif strChoice.strip() == "5":
            break

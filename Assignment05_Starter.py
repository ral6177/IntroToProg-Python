# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (When,Who, What):
# 1.1.2030,RRoot,Created started script
# 2021-02-15, rlopez,
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
"""  # A menu of user options
# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (likeLab 5-2)
# TODO: Add Code Here

file = open(objFile,"r")
for item in file:
    lstRow = item.split(",") # split the rows in the file based on comma, assign to lstRow variable
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()} # assign list 0 and 1 to dicRow dictionary
    lstTable.append(dicRow) # add dictionary to lstTable variable
file.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        print("Here's your Task List, with Priority: ")
        for dicRow in lstTable:
            print(dicRow["Task"] + ', ' + dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        print("Add new time to the list")
        taskItem = input("Please enter the task: ")
        taskPriority = input("Please enter the task priority: ")
        dicRow = {"Task": taskItem, "Priority": taskPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove an item from the list/Table based on its name
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        print("Remove item from the list")
        print("Below are the current items in the list: ")
        for dicRow in lstTable:
            print(dicRow["Task"] + ', ' + dicRow["Priority"])
        taskRemove = input("Enter the name of the task you want to remove:")
        for item in lstTable:
            if item["Task"] == taskRemove:
                lstTable.remove(item)
            else:
                print("Could not find task")
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        file = open(objFile, "w")
        for item in lstTable:
            file.write(item["Task"] + "," + item["Priority"] + "\n")
        file.close()
        print("To do item saved to list")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("We're done here. Go enjoy the snow")
        break  # and Exit the program



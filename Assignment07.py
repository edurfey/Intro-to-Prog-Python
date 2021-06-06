# ----------- #
# Title: Listing 9
# Description: An example of storing data in a binary file
# Changelog: (Who, What, When)
# EDurfey, 6/2/21, Created scripts
# ----------- #


import pickle

# Demo the program #
customer_id = int(input("Enter an ID: "))
customer_name = str(input("Enter a name: "))
customer_list = [customer_id, customer_name]
print(customer_list)

# Store the data with the pickle.dump method #
objFile = open("AppData.dat", "ab")
pickle.dump(customer_list, objFile)
objFile.close()

# Read the data back with pickle.load #
objFile = open("AppData.dat", "ab")
objFileData = pickle.load(objFile)
objFile.close()
print(objFileData)


# Error Handling Data #

# Demo 1

try:
   quotient = 10/0
    print(quotient)
    except
    print("There was an error!")

# Demo 2

 try:
    quotient = 10/0
    print(quotient)
 except Exception as E:
   print("There was an error!")
   print("Built-in Python error message info: ")
   print("E")
   print(type(E))
   print(E._doc_)
   print(E._str_())

# Demo 3

try:
    quotient = 10/0
    print(quotient)
except ZeroDivisionError as e:
    print("Please do not use zero as the second number!")
    print(E, E_doc_, type(E), sep='\n')
except Exception as e:
    print("There was an error!")
    print(E, E._doc_, type(E), sep='\n')

# Testing Both #
 try
   customer_id = int(input("Enter an ID: "))
   customer_name = str(input("Enter a name: "))
   customer_list = (customer_id, customer_name)
   print(customer_list)
 except Exception as E:
   print("There was an error! Use integers for IDs")
   print(E,E._doc_, type(E), sep='\n')

# Store the data using the pickle dump method #
try:
   file = open("AppData.dat", "ab")
   pickle.dump(customer_list, file)
   file.close()
 except Exception as E:
   print("There was an error! Check file permissions!")
   print(E,E._doc_, type(E), sep='\n')

# Read back the data using the pickle.load method #
try:
   file = open("AppData.dat", "ab")
   file_data = pickle.load(file)
   file.close()
   print(file_data)
 except FileNotFoundError as E:
   print("The file must exist before trying to read it!")
   print(E,E._doc_, type(E), sep='\n')
 except Exception as E:
   print("There was a general error!")
   print(E,E._doc_, type(E), sep='\n')



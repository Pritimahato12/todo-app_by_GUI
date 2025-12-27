#print("Enter todo: ")#argument of the function print
# user_prompt = "Enter todo : "
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
# todo4 = input(user_prompt)

# todos = [todo1, todo2, todo3, todo4]
# print(todos)

# print(type(user_prompt))
# print(type(todos))

#https://www.udemy.com/course/the-python-mega-course/learn/lecture/42469640#content
#https://www.udemy.com/course/the-python-mega-course/learn/lecture/46117853#content


#batch operation in python--->use while loop

# while True:
#   todo=input(user_prompt)
#   print(todo)
#   print("Next...")
  
#store the todos in a list 
# while True:
#   todo=input(user_prompt)
#   todos=[todo]#it overwrites the existing list
#   print(todos)

# thats why we use python methods
# user_prompt = "Enter todo : "
# todos=[]#list is an object
# every objects has its own methods
# while True:
#   todo=input(user_prompt)
#   # print(todo.capitalize())
#   print(todo.title())
#   todos.append(todo) #here append methods is a part of the object
#   print(todos)
  
# "add" != "add "
# strip method --> removes the trailing space from the string   --->  user_action = user_action.strip()

#enumerate = it makes avalable not only the items of the list but also the indices of the list
# srings can also use enumerate function

# a=enumerate(['a', 'b', 'c'])
# print(list(a))

#how to store the data in an external file on disk 
#first method --> text file (csv or json file)

# todos=[]

#to remove "\n" we use list comprehension

#list comprehension--> is equivalent to for loop --> it's the another method to modify the items in the list

#######################################################################################################################################################

# while True:
#   user_action = input("Type add, show,edit, exit and completed : ")
#   user_action = user_action.strip()
  
#   match user_action:
#     case 'add':
#       todo = input("Enter a todo: ") + "\n"
      
#       # file = open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r')
#       # todos = file.readlines()
#       # file.close()
      
#       #web complex manager-->with --->do the same thing whichi we do above it
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#         todos = file.readlines()
      
#       todos.append(todo)
      
#       # file = open('todos.txt', 'w')#it produces certain type of just like a string object # interact with the text file pass the name of the text file 
#       # #and second argument we haveto give any 1 of this: 'w','r'
#       # file.writelines(todos) 
#       # file.close()
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'w') as file:
#         file.writelines(todos)
    
      
#     case 'show' | 'display':
#       # for item in todos:
#       #   item= item.title()
#       #   print(item)
      
      
#       # file = open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r')
#       # todos = file.readlines()
#       # file.close()
      
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#         todos = file.readlines()
        
        
#       # new_todos = [] 
      
#       #list comprhension
#       # for item in todos:
#       #   new_item = item.strip('\n')
#       #   new_todos.append(new_item)
      
#       #...................OR.....................
        
#       # new_todos = [item.strip('\n') for item in todos]
      
#       # for index, item in enumerate(new_todos):
#       for index, item in enumerate(todos):
#         item=item.strip('\n')
#         item= item.title()
#         # print(index, '-', item)
#         print(f"{index + 1}: {item}")
        
        
#     case 'edit':
#       number = int(input("Number of the todo to edit: "))
#       number = number -1
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#         todos = file.readlines()
#       # print('here is todos existing',todos)
      
      
#       new_todo = input("Enter new todo: ")
#       todos[number] = new_todo + "\n"
#       # existing_todo = todos[number]
#       # print(existing_todo)
#       # print('here is how it will be ',todos)
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'w') as file:
#         file.writelines(todos)
      
#     case 'exit':
#       break
    
    
#     case 'completed' | 'done':
#       number = int(input("Number of the todo to complete: "))
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#         todos = file.readlines()
      
#       index = number - 1  
#       todo_to_remove = todos[index].strip('\n') 
#       todos.pop(index)
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'w') as file:
#         file.writelines(todos)
      
#       message = f"Todo {todo_to_remove} was removed from the list"
      
#       print(message)
#     case _:
#       print("Hey, you entered an unknown command")
    
# print("Bye")

##########################################################################################################################################################

# while True:
#   user_action = input("Type add, show,edit, exit and completed : ")
#   user_action = user_action.strip()
  
#   if 'add' in user_action or 'new' in user_action:
#     #list slicing
#     todo = user_action[4:]#it strip out the add part just print after the add portion
    
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#       todos = file.readlines()
      
#     todos.append(todo + "\n")
      
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'w') as file:
#       file.writelines(todos)
    
      
#   elif 'show' in user_action or 'display' in user_action or 'view' in user_action:
      
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#       todos = file.readlines()
      
#     for index, item in enumerate(todos):
#       item=item.strip('\n')
#       item= item.title()
#       # print(index, '-', item)
#       print(f"{index + 1}: {item}")
        
        
#   elif 'edit' in user_action:
#     number = int(user_action[5:])
#     print(number)
#     number = number -1
    
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#       todos = file.readlines()
    
    
#     new_todo = input("Enter new todo: ")
#     todos[number] = new_todo + "\n"
    
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'w') as file:
#       file.writelines(todos)
      
#   elif 'exit' in user_action:
#     break
    
    
#   elif 'completed' in user_action or 'done' in user_action:
#     number = int(user_action[10:])
#     print(number)
    
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#       todos = file.readlines()
    
#     index = number - 1  
#     todo_to_remove = todos[index].strip('\n') 
#     todos.pop(index)
    
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'w') as file:
#       file.writelines(todos)
    
#     message = f"Todo {todo_to_remove} was removed from the list"
    
#     print(message)
  
#   else:
#     print("Command is not valid")
    
# print("Bye")

#############################################################################################################################################################

# while True:
#   user_action = input("Type add, show,edit, exit and completed : ")
#   user_action = user_action.strip()
  
#   if user_action.startswith("add") or user_action.startswith("new"):
#     #list slicing
#     todo = user_action[4:]#it strip out the add part just print after the add portion
    
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#       todos = file.readlines()
      
#     todos.append(todo + "\n")
      
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'w') as file:
#       file.writelines(todos)
    
      
#   elif user_action.startswith("show") or user_action.startswith('display') or user_action.startswith('view'):
      
#     with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#       todos = file.readlines()
      
#     for index, item in enumerate(todos):
#       item=item.strip('\n')
#       item= item.title()
#       # print(index, '-', item)
#       print(f"{index + 1}: {item}")
        
        
#   elif user_action.startswith("edit"):
#     #error handling
#     try:  
#       number = int(user_action[5:])
#       print(number)
#       number = number -1
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#         todos = file.readlines()
      
      
#       new_todo = input("Enter new todo: ")
#       todos[number] = new_todo + "\n"
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'w') as file:
#         file.writelines(todos)
#     except ValueError:
#       print("Your command is not valid.")
#       # user_action = input("Type add, show,edit, exit and completed : ")
#       # user_action = user_action.strip()
#       continue
      
#   elif user_action.startswith("completed") or user_action.startswith("done"):
#     try:  
#       number = int(user_action[10:])
#       print(number)
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'r') as file:
#         todos = file.readlines()
      
#       index = number - 1  
#       todo_to_remove = todos[index].strip('\n') 
#       todos.pop(index)
      
#       with open(r'C:\Users\RIYA\OneDrive\Desktop\python_programs\python-mega-course\project\to-do-list-app\main-code\todos.txt', 'w') as file:
#         file.writelines(todos)
      
#       message = f"Todo {todo_to_remove} was removed from the list"
      
#       print(message)
#     except IndexError:
#       print("There is no item with that number")
#       continue
  
#   elif user_action.startswith('exit'):
#     break
  
#   else:
#     print("Command is not valid")
    
# print("Bye")

#############################################################################################################################################################


#custom functions:
# path = 'C:/Users/RIYA/OneDrive/Desktop/python_programs/python-mega-course/project/to-do-list-app/main-code/todos.txt'

# def get_todos(filepath = path):#here parameter is passed
#   """ Read a text file and return the list of
#   to-do-items
#   """
#   with open(filepath, 'r') as file_local:
#     todos_local = file_local.readlines()
#   return  todos_local

# # print(help(get_todos))

# # def write_todos(filename , todos_arg):
# def write_todos(todos_arg, filename = path):
#   """ write the to-do items list in the text file"""
#   with open(filename, 'w') as file:
#     file.writelines(todos_arg)
    

# text = """
# principals of productivity:
# Managing your inflow.
# Systemizing everything that repeats
# """

# print(text)

#variable scope here todos is under def fuction which is not accesssible outside that function
#print(todos)  it will give an error
#here todos variable is local variable
#here outside the scope the defined variable  is known as global variable

# while True:
#   user_action = input("Type add, show,edit, exit and completed : ")
#   user_action = user_action.strip()
  
#   if user_action.startswith("add") or user_action.startswith("new"):
#     #list slicing
#     todo = user_action[4:]#it strip out the add part just print after the add portion
    
#     todos = get_todos()  #function call --> here the argument is passed
      
#     todos.append(todo + "\n") # Attribute error-->means the method does not exist for that object
      
#     write_todos(todos)
    
      
#   elif user_action.startswith("show") or user_action.startswith('display') or user_action.startswith('view'):
      
#     todos = get_todos()
      
#     for index, item in enumerate(todos):
#       item=item.strip('\n')
#       item= item.title()
#       # print(index, '-', item)
#       print(f"{index + 1}: {item}")
        
        
#   elif user_action.startswith("edit"):
#     #error handling
#     try:  
#       number = int(user_action[5:])
#       print(number)
#       number = number -1
      
#       todos = get_todos()
      
      
#       new_todo = input("Enter new todo: ")
#       todos[number] = new_todo + "\n"
      
#       write_todos(todos)
      
      
#     except ValueError:
#       print("Your command is not valid.")
#       # user_action = input("Type add, show,edit, exit and completed : ")
#       # user_action = user_action.strip()
#       continue
      
#   elif user_action.startswith("completed") or user_action.startswith("done"):
#     try:  
#       number = int(user_action[10:])
#       print(number)
      
#       todos = get_todos()
      
#       index = number - 1  
#       todo_to_remove = todos[index].strip('\n') 
#       todos.pop(index)
      
#       write_todos(todos)
      
#       message = f"Todo {todo_to_remove} was removed from the list"
      
#       print(message)
#     except IndexError:
#       print("There is no item with that number")
#       continue
  
#   elif user_action.startswith('exit'):
#     break
  
#   else:
#     print("Command is not valid")
    
# print("Bye")

# ...

#########################################################################################################################################
#FRONTENED
#from module(dir) import functions
# from functions import get_todos, write_todos
import functions
# todos = functions.get_todos() -->like a method but the diff is here it is a module
import time

now = time.strftime("%b -%d, %Y %H:%M:%S")
print("It is", now)

while True:
  user_action = input("Type add, show,edit, exit and completed : ")
  user_action = user_action.strip()
  
  if user_action.startswith("add") or user_action.startswith("new"):
    #list slicing
    todo = user_action[4:]#it strip out the add part just print after the add portion
    
    todos = functions.get_todos()  #function call --> here the argument is passed
      
    todos.append(todo + "\n") # Attribute error-->means the method does not exist for that object
      
    functions.write_todos(todos)
    
      
  elif user_action.startswith("show") or user_action.startswith('display') or user_action.startswith('view'):
      
    todos = functions.get_todos()
      
    for index, item in enumerate(todos):
      item=item.strip('\n')
      item= item.title()
      # print(index, '-', item)
      print(f"{index + 1}: {item}")
        
        
  elif user_action.startswith("edit"):
    #error handling
    try:  
      number = int(user_action[5:])
      print(number)
      number = number -1
      
      todos = functions.get_todos()
      
      
      new_todo = input("Enter new todo: ")
      todos[number] = new_todo + "\n"
      
      functions.write_todos(todos)
      
      
    except ValueError:
      print("Your command is not valid.")
      # user_action = input("Type add, show,edit, exit and completed : ")
      # user_action = user_action.strip()
      continue
      
  elif user_action.startswith("completed") or user_action.startswith("done"):
    try:  
      number = int(user_action[10:])
      print(number)
      
      todos = functions.get_todos()
      
      index = number - 1  
      todo_to_remove = todos[index].strip('\n') 
      todos.pop(index)
      
      functions.write_todos(todos)
      
      message = f"Todo {todo_to_remove} was removed from the list"
      
      print(message)
    except IndexError:
      print("There is no item with that number")
      continue
  
  elif user_action.startswith('exit'):
    break
  
  else:
    print("Command is not valid")
    
print("Bye")


#***************************************************************************************************************************

#Versions of the program::

#is the skill of controlling the version of your programs  --> version control
#it is a practice that allows you to track changes in your code and manage those changes

#**************************************************************************************************************************************
#***************************************************************************************************************************

#time module

#time.strftime("%Y") --> '2025'
#time.strftime("%m - %Y") --> '26 - 2025'
#time.strftime("%b") --> 'December'
#time.strftime("%b -%d, %Y %H:%M:%S") --> 'December 26, 2025 22:03:40'

#https://docs.python.org/3/library/datetime.html

#**************************************************************************************************************************************

#***************************************************************************************************************************

#csv module

#glob
#webbrowser
#shutil

#**************************************************************************************************************************************

#***************************************************************************************************************************

#GIT CHECKOUT

#GIT RESET

#**************************************************************************************************************************************

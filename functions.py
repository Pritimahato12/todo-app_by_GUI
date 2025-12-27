#BACKENED

FILEPATH = 'C:/Users/RIYA/OneDrive/Desktop/python_programs/python-mega-course/project/to-do-list-app/main-code/todos.txt'

def get_todos(filepath = FILEPATH):#here parameter is passed
  """ Read a text file and return the list of
  to-do-items
  """
  with open(filepath, 'r') as file_local:
    todos_local = file_local.readlines()
  return  todos_local

# print(help(get_todos))

# def write_todos(filename , todos_arg):
def write_todos(todos_arg, filename = FILEPATH):
  """ write the to-do items list in the text file"""
  with open(filename, 'w') as file:
    file.writelines(todos_arg)

# print(type(__name__))    
# print(__name__)

#the __name__ variable is hiddenly defined
if __name__ == "__main__" :
  print("hello from functions")
  print(get_todos())
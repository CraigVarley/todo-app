#functions

#read the text file
def get_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:  # context manager
        todos_local = file_local.readlines()
    return todos_local

# write the text file
def write_todos(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# list the todos from read file
def enumerate_todos(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:  # context manager
        todos_local = file_local.readlines()
    for number, item in enumerate(todos_local):
        item = item.strip('\n')
        row = f"{number + 1}-{item}"
        print(row)





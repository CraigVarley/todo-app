import functions
import time

todos = []

while True:
    print(time.strftime("Right now it's %c"))
    user_input = input("Type add, show, edit, complete, or exit:")
    user_input = user_input.strip()

    if user_input.startswith('add'):

            todo = user_input[4:] + '\n'

            todos = functions.get_todos()

            todos.append(todo)

            functions.write_todos(todos, 'todos.txt')

            functions.enumerate_todos(todos)

    elif user_input.startswith('show'):

        todos = functions.get_todos()

        functions.enumerate_todos(todos)

    elif 'exit' in user_input:

        break

    elif user_input.startswith('edit'):
        try:
            number = int(user_input[5:])
            number = number-1

            todos = functions.get_todos()

            new_todo = input('Add new todo: ')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, 'todos.txt')

            functions.enumerate_todos(todos)

        except ValueError:
            print("Your command is not valid. Enter a number after edit, e.g. edit 3")
            continue

    elif user_input.startswith('complete'):

        number = int(input('Which todo do you want to remove?'))

        todos = functions.get_todos()

        todo_to_remove = todos[number-1].strip('\n')

        todos.pop(number-1)

        functions.write_todos(todos,'todos.txt')

        print(f'Todo {todo_to_remove} was removed')

    else:
        print('Not valid. Enter one of the keywords: add, show, complete, edit, exit.')
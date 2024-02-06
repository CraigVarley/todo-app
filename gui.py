import functions
import PySimpleGUI as sg
import time
import os

#create file if not exists
if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

sg.theme('Black')

clock = sg.Text('', key="clock")
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
calendar = sg.CalendarButton("Choose A Complete By Time and Date", key="cal")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")


# window instance, Python doesn't have window instances by default, need 3rd party
window = sg.Window('My App',
                   layout=[[clock],
                           [label, input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]], # *** inner square brackets are one row ***
                   font=('Helvetica', '10'))
while True:
    event, values = window.read(timeout=10) #button event and input value
    # TIMEOUT REQUIRD OTHERWISE THIS ONLY RUNS ON AN EVENT AND CLOCK NEEDS REFRESHING
    window['clock'].update(value=time.strftime('%c'))
    match event:
        case "Add":
            todos_list = functions.get_todos()
            new_todo = values['todo'] + '\n'
            if new_todo == '\n':
                sg.Popup('Write something you beautiful fool.')
            else:
                todos_list.append(new_todo)
                functions.write_todos(todos_list)
                window['todos'].update(values=todos_list)
                window['todo'].update(value='')
        case "Edit":
            try:
                todo_edit = values['todos'][0] # get event value
                new_todo = values[('todo')] #get text box value

                todos_list = functions.get_todos() #save todos list from txt file
                todos_edit_index = todos_list.index(todo_edit) # get index of editing todo
                todos_list[todos_edit_index] = new_todo #add new todo to same index
                functions.write_todos(todos_list) # write to txt file
                window['todos'].update(values=todos_list)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=['Helvetica', 11])
        case "todos":
            window['todo'].update(value=values['todos'][0]) #all instances assigned to window
        case "Exit":
            sg.WIN_CLOSED
            break
        case "cal":
            date = values['Calendar']
            print(date)
        case "Complete":
            try:
                # get selected todo
                completed_todo = values['todo']
                # delete from todos.txt
                todos_list = functions.get_todos()
                todos_list.remove(completed_todo)
                functions.write_todos(todos_list)
                window['todos'].update(values=todos_list)
                window['todo'].update(value='')
                # delete from list
            except ValueError:
                sg.popup("Please select an item first", font=['Helvetica', 11])
        case sg.WIN_CLOSED:
            break

window.close()


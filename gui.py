import functions
import PySimpleGUI as sg


label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")


# window instance, Python doesn't have window instances by default, need 3rd party
window = sg.Window('My App',
                   layout=[[label, input_box, add_button]], # *** inner square brackets are one row ***
                   font=('Helvetica', '10'))
while True:
    event, values = window.read() #button event and input value
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()


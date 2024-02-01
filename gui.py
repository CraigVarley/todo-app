import functions
import PySimpleGUI as sg


label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")


# window instance, Python doesn't have window instances by default, need 3rd party
window = sg.Window('My App', layout=[[label, input_box, add_button]]) #layout expects a list of instances
# *** inner square brackets are one row ***

window.read()
window.close()


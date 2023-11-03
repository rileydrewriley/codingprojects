import PySimpleGUI as sg
from functions import get_meters

feetLabel = sg.Text("Enter feet: ")
inchesLabel = sg.Text("Enter inches: ")
input1 = sg.Input(key="feet")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor", layout=[[feetLabel, input1],
                                        [inchesLabel, input2],
                                        [convert_button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = get_meters(feet, inches)
    window["output"].update(value=f"{result} m")

window.read()
window.close()

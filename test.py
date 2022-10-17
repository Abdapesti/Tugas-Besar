import PySimpleGUI as sg

sg.theme("DarkAmber")
layout = [
    [sg.Button("+"), sg.Text("0", key = "-TEXT-"), sg.Button("-")]
]

window = sg.Window("Vending Machine", layout)

while True:
    event, values = window.read()
    if event == "+":
        window["-TEXT-"].update("0")
    break



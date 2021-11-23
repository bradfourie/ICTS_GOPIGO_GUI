import PySimpleGUI as sg
from classes import *
from matplotlib.figure import Figure

# Initialising the client and connecting to the server
client = Client()
client.connect()

sg.ChangeLookAndFeel('Black')

fig = Figure()

ax = fig.add_subplot(111)
ax.set_xlabel("X position")
ax.set_ylabel("Y position")
ax.grid()

control_paradigm_list = ['Free Roaming', 'Follow Left Wall', 'Follow Right Wall', 'User Control']
#manual_speed_list = ['100', '200', '300' , '400', '500', '1000']

control_and_status_column = [
        [
            sg.Frame(layout=[
                [sg.Text('Battery Voltage:', size=(16,1),  font=("Helvetica", 14), justification='left'), sg.Text('13.8V', size=(16,1),  font=("Helvetica", 14), justification='left', key='battery_voltage_txt')],
                [sg.Text('IP Address:', size=(16,1),  font=("Helvetica", 14), justification='left'), sg.Text(SERVER_IP, size=(16,1),  font=("Helvetica", 14), justification='left')],
            ], title='Robot Status', font=("Helvetica", 18), element_justification='centre', relief=sg.RELIEF_SUNKEN),
        ],
        [
            sg.Frame(layout=[
                [sg.Text('Select Control Paradigm:', size=(30,1),  font=("Helvetica", 16), justification='left')],
                [sg.Combo(control_paradigm_list, default_value='Free Roaming', key='CONTROL_PARADIGM')],
                [sg.Button('Select', size=(8,1))],
                [sg.Text('Control Override Buttons:', size=(30,1),  font=("Helvetica", 16), justification='left')],
                [sg.Button('START', size=(15,1))],
                [sg.Button('STOP',size=(15,1))],
            ], title='Control Override', font=("Helvetica", 18), element_justification='centre', relief=sg.RELIEF_SUNKEN),
        ],
        [
            sg.Frame(layout=[
                [sg.Text('Button Override:', size=(30,1),  font=("Helvetica", 16), justification='left')],
                [sg.Button('W', size=(2,1))],
                [sg.Button('A', size=(2,1)), sg.Button('S', size=(2,1)), sg.Button('D', size=(2,1))],
            ], title='Manual Control', font=("Helvetica", 18), element_justification='centre', relief=sg.RELIEF_SUNKEN),
        ],

]

layout = [
    [sg.Text('GoPiGo3 Control Panel', size=(22, 1), justification='center', font=("Helvetica", 22), relief=sg.RELIEF_RIDGE)],
    [
            sg.Column(control_and_status_column),
    ]
]

#window = sg.Window(title="BTGoPiGo ICTS WiSe2021", layout=layout, margins=(100, 100)).read()  #remove this read?
window = sg.Window(title="BTGoPiGo ICTS WiSe2021", layout=layout, margins=(150, 150))

while True:
    event, values = window.read()

    battery_voltage = client.receive_message()
    if battery_voltage is not None:
        window['battery_voltage_txt'].update(battery_voltage + "V")

    if event == sg.WIN_CLOSED:
        break

    if  event == 'Select':
        combo = values['CONTROL_PARADIGM']
        if combo == "Follow Left Wall":
            message = "LEFT_WALL"
            client.send_message(message)
        elif combo == "Follow Right Wall":
            message = "RIGHT_WALL"
            client.send_message(message)
        elif combo == "Free Roaming":
            message = "FREE_ROAMING"
            client.send_message(message)
        elif combo == "User Control":
            message = "USER_CONTROL"
            client.send_message(message)
        print('CONTROL_PARADIGM Sent')
    elif event == 'START':
        client.send_message(event)
        print('START Sent')
    elif  event == 'W':
        client.send_message(event)
        print('W Sent')
    elif event == 'A':
        client.send_message(event)
        print('A Sent')
    elif event == 'S':
        client.send_message(event)
        print('S sent')
    elif event == 'D':
        client.send_message(event)
        print('D Sent')
    elif event == 'STOP':
        client.send_message(event)
        print('STOP Sent')






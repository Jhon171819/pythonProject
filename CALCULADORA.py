import PySimpleGUI as sg
Re = 0
sg.theme('DarkAmber')
sg.set_options(font='Calibri 25')
numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
num = ''
full_op= ''
layout = [
    [sg.Txt('calculadora em Python', justification='right', expand_x=True,key='-text-')],
    [sg.Button('Limpar', expand_x=True)],
    [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('4'), sg.Button('5'), sg.Button('+')],
    [sg.Button('6'), sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('0'), sg.Button('-')],
    [sg.Button('*'), sg.Button('/')],
    [sg.Button('Enter', expand_x= True)]
]

janela = sg.Window("caluladora", layout)

while True:
    events, values = janela.read()

    if events in numero:
        num+= events
        num_string = num

        janela['-text-'].update(f'{full_op} {num_string}')


    if events == 'Limpar':
        num = ''
        num_string =''
        full_op = ''
        janela['-text-'].update('   ')
        janela.read()


    if events in ['-','+','*','/']:
        full_op+= num
        num= ''
        full_op+=events
        

        janela['-text-'].update(full_op)



    if events == 'Enter':
        full_op+=num


        

        result = eval((full_op))

        janela['-text-'].update('{:.0f}'.format(result))

    if events == sg.WINDOW_CLOSED:
        break



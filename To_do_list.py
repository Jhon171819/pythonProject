import PySimpleGUI as sg
tarefas = []
def Todo():
    sg.theme('DarkAmber')
    layout = [
        [sg.Text('Lista de atividades', expand_x= True)],
        [sg.Input(key='AT')],
        [sg.Text('', key='atv')],
        [sg.Button('Adicionar'),sg.Button('Resetar')]
    ]
    return sg.Window('To do list', layout=layout, finalize= True)

janela = Todo()

while True:
    events, valores = janela.read()
    if events == 'Adicionar':

        tarefas.append(valores['AT'])
        janela.extend_layout(janela['atv'], [
            [sg.Text(valores['AT'], key='tt'), sg.Button('Excluir')]
        ])

    if events == 'Excluir':
        texto= janela['tt']
        texto.update('')
    if events == 'Resetar':
        janela.close()
        janela = Todo()



    if events == sg.WINDOW_CLOSED:
        break


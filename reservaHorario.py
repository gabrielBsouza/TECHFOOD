import this
import menu
this.opcao = 0
def escolhaHorario():
    print('Escolha um dos horários abaixo:\n' +
        "\n1. 20:00/20:30" +
        "\n2. 20:30/21:00" +
        "\n3. 21:00/21:30" )
    this.opcao = int(input())

def operacao():
        # Mostrar o menu em tela
    while this.opcao != 1 or 2 or 3:
        escolhaHorario()
        # realizar operações
        if this.opcao == 1:
            print("Horário da reserva confirmado entre 20:00/20:30")
            menu.Menu()
        elif this.opcao == 2:
            print("Horário da reserva confirmado entre 20:30/21:00")
            menu.Menu()
        elif this.opcao == 3:
            print("Horário da reserva confirmado entre 21:0/21:30")
            menu.Menu()
        else:
            print('Opcao escolhida inválida! Tente novamente com as opções fornecidas.')
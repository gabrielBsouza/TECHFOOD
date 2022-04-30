import this
import hamburgao
import pizza
import bauru

this.opcao = 0
def Menu ():
    print('Escolha uma das opções abaixo:\n'+
          '\n1. Hamburgão R$5,00'+
          '\n2. Pizza R$5,00'+
          '\n3. Bauru R$5,00'+
          '\n4. Fechar Programa')
    this.opcao = int(input())

def operacao():
    #Mostrar o menu em tela
    while this.opcao != 6:
        Menu()
        #realizar operações
        if this.opcao == 1:
            #operacao para 1.
            hamburgao.operacao()
        elif this.opcao == 2:
            #operacao para 2.
            pizza.operacao()
        elif this.opcao == 3:
            # operacao para 3.
            bauru.operacao()
        elif this.opcao == 4:
            print('Fechando... agradecemos sua presença aqui!')
        else:
            print('Opção escolhida inválida! Tente novamente com as opções fornecidas.')
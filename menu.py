import this
import hamburgao
import pizza
#import salgadoFrango
#import salgadoQueijo
#import bauru


this.opcao = 0 #Criar a variavel global
def Menu ():
    print('Escolha uma das opções abaixo:\n'+
          '\n1. Hamburgão R$5,00'+
          '\n2. Pizza R$5,00'+
          #'\n3. Salgado de Frango R$5,00'+
          #'\n4. Salgado de Queijo R$5,00'+
          #'\n5. Bauru R$5,00'+
          '\n6. Fechar Programa')
    this.opcao = int(input())

def operacao():
    #Mostrar o menu em tela
    while this.opcao != 6:
        Menu()
        #realizar operações
        if this.opcao == 1:
            #operacao para 1.
            hamburgao.coletar()
        elif this.opcao == 2:
            #operacao para 2.
            pizza.operacaoPizza()

        elif this.opcao == 6:
            print('Fechando... agradecemos sua presença aqui!')
        else:
            print('Opcao escolhida inválida! Tente novamente com as opções fornecidas.')
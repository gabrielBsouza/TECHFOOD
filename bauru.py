import this
import reservaBauru
this.precoBauru = 5
this.quantBauru = 10
this.quantidade = 0
this.opcao = 0
def Preco ():
    print('O preco do Hamburgão é: R$' + str(this.precoBauru) + ',00.')

def Quantidade ():
    print('A quantidade disponível desse lanche é: ' + str(this.quantBauru) + '.')

def Selecao ():
    print('Digite a quantidade que deseja comprar: ')
    this.quantidade = int(input())
    while (this.quantidade < 0) or (this.quantidade > this.quantBauru):
        if (this.quantidade < 0) or (this.quantidade > this.quantBauru):
            print('Informe uma quantidade acessível à disponível, por favor!')
            this.quantidade = int(input())
    this.quantBauru = this.quantBauru - this.quantidade

def Calculo():
    return this.quantidade * this.precoBauru

def Compra ():
    Preco()
    Quantidade()
    Selecao()
    print('---------------- O valor total da compra é: '+ str(Calculo()) +',00. ----------------\n')
def Menu ():
    Compra()
    print('Deseja:'
          '\n1. Realizar Compra' +
          '\n2. Realizar reserva'+
          '\n3. Cancelar Compra')
    this.opcao = int(input())

def operacao():
    Compra()
    while this.opcao != 6:
        Menu()
        #realizar operações
        if this.opcao == 1:
            #operacao para 1.
            print('O código do PIX é 12345678912, acesse https://www.picpay.com/site para efetuar pagamento.')
        elif this.opcao == 2:
            #opereção para 2.
            reservaBauru.coletar()
        elif this.opcao == 3:
            print('Fechando... agradecemos sua presença aqui!')
        else:
            print('Opção escolhida inválida! Tente novamente com as opções fornecidas.')
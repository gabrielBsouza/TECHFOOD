import this
import menu
import reserva
this.pizzas = 5.00
this.quantidade = 10
this.opcao = 0  # Criar a variavel global

def coletar():
    print("Informe seu nome completo\n ")
    this.dados = float(input)
    print("A quantidade de pizzas é: "+ this.quantidade + ". Deseja Comprar quantas pizzas? :")
    this.quantidadePizzas = float(input)

def calcular():
    coletar()
    this.precoPizzas = this.quantidadePizzas * this.pizzas
    this.quantidadeRestante = this.quantidade - this.quantidadePizzas

def mostrar():
    coletar()
    calcular()
    print("O valor da sua compra ficou: " + this.precoPizzas )


def mostrarMenu():
    print("Escolha uma das Opções Abaixo!\n " +
          "\n1. Desejo apenas reservar meu produto " +
          "\n2. Não!!!, desejo escolher outro produto ;)" +
          "\n3. Sim!!!, desejo Confirmar minha compra :)")
    this.opcao = int(input())  # Comando para coletar oq o usuario irá digitar

def operacaoPizza():
    coletar()
    calcular()
    mostrar()
    mostrarMenu()
    # Mostrar o Menu em tela
    while this.opcao != 3:
        mostrarMenu()
        # Realizar as operções
        if this.opcao == 1:
            print("Produto no nome de," + this.dados + ", no valor de " + this.precoPizzas + ", RESERVADO!!")
        elif this.opcao == 2:
            this.quantidadeRestante = this.quantidade
            menu.Menu()
        elif this.opcao == 3:  ## opção para fechar
            print("Faça o pagamento através do PIX '61985181121'Obrigado pela preferência!" + this.dados)
        else:
            print("Opção Escolhida Inválida, tente outra vez!")

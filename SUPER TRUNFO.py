import random

gabarito = ["Nome", "Velocidade", "Tanque", "Ano"]

baralho = [
    ["Ferrari F40", 324, 120, 1987],
    ["Toyota Yaris", 175, 36, 2024],
    ["Audi R8", 330, 83, 2021],
    ["Bugatti Chiron", 420, 100, 2016],
    ["Porsche 911", 310, 64, 2023],
    ["McLaren P1", 350, 72, 2013],
    ["BYD Song", 170, 60, 2023],
    ["Lamborghini", 350, 90, 2011]
]

random.shuffle(baralho)

jogador1 = []
jogador2 = []

for carta in baralho:

    if len(jogador1) <= len(jogador2):
        jogador1.append(carta)

    else:
        jogador2.append(carta)

monte = []

def mostrar_carta(carta):

    print("\nCarta:")

    for atributo in range(len(gabarito)):
        print(atributo, "-", gabarito[atributo], ":", carta[atributo])

while True:

    print("\n==== SUPER TRUNFO ====")
    print("1 - Single Player")
    print("2 - Multiplayer")
    print("3 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 3:
        print("Fim do jogo")
        break

    elif opcao == 1 or opcao == 2:

        vez = 1

        while len(jogador1) > 0 and len(jogador2) > 0:

            print("\n-------------------")
            print("Jogador 1:", len(jogador1), "cartas")
            print("Jogador 2:", len(jogador2), "cartas")

            carta_jogador1 = jogador1[0]
            carta_jogador2 = jogador2[0]

    
            if vez == 1:

                print("\nVEZ DO JOGADOR 1")

                mostrar_carta(carta_jogador1)

                atributo_escolhido = int(input("\nDigite atributo (1 a 3): "))

            else:

               
                if opcao == 1:

                    atributo_escolhido = random.randint(1, 3)

                    print("\nCOMPUTADOR ESCOLHEU:",
                          gabarito[atributo_escolhido])

                else:

                    print("\nVEZ DO JOGADOR 2")

                    mostrar_carta(carta_jogador2)

                    atributo_escolhido = int(input("\nDigite atributo (1 a 3): "))

            valor_jogador1 = carta_jogador1[atributo_escolhido]
            valor_jogador2 = carta_jogador2[atributo_escolhido]

            print("\nJogador 1:", valor_jogador1)
            print("Jogador 2:", valor_jogador2)

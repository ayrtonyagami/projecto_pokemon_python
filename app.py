from ast import While
import random
import pickle

from Pokemon import *
from pessoa import *


def escolher_pokemon_inicial(player):
    
    pikachu = PokemonElectrico("Pikachu")
    charmander = PokemonFogo("Charmander")    
    curvina = PokemonAgua("Curvina")
    
    while True:
        print("{} escolha um pokemon para dar inicio a tua jornada".format(player.nome))
        print("1 - ",pikachu)
        print("2 - ",charmander)
        print("3 - ",curvina)
        escolha = input("Escolha o seu pokemon: ")

        if escolha == "1":
            player.pokemons.append(pikachu)
            break
        elif escolha == "2":
            player.pokemons.append(charmander)
            break
        elif escolha == "3":
            player.pokemons.append(curvina)
            break
        else:
            print("Escolha errada!")

def salvar_jogo(player):
    try:
        with open("basedados.db","wb") as arquivo:
            pickle.dump(player,arquivo)
            print("Jogo salvo")
    except Exception as ex:
        print("Erro ao tentar salvar na base de dados")
        print(ex)


def carregar_jogo():
    try:
        with open("basedados.db","rb") as arquivo:
            player = pickle.load(arquivo)
            print("Jogo carregado")
            return player
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    print("================================")
    print("==   POKEMON RGP YAGAMILAND   ==")
    print("================================")

    player =  carregar_jogo()

    if not player:

        print("Vamos começar a jornada do pokemon")
        nome_do_jogador = input("Qual é o teu nome? ")
        player = Player(nome_do_jogador)
        print("Seja muito bem-vindo {}, essa jornada será divertida.".format(nome_do_jogador))
        input()
        player.mostrar_dinheiro()
        input()

        if player.pokemons:
            print("Você já tem alguns pokemons")
            player.mostrar_pokemons()
        else:
            escolher_pokemon_inicial(player)

        print("Pronto, agora que você já tem pokemon, enfrenta seu arqui-rival deste o jardim da infância, o Gary!")
        inimigo = Inimigo("Gary")
        player.batalhar(inimigo)

        salvar_jogo(player)
    else:
        print(player, "bem-vindo de volta!!!")

    while True:
        print("======================================")
        print("O que deseja fazer")
        print("1 - Explorar")
        print("2 - Lutar contra um iminigo")
        print("3 - Poke-agenda")
        print("4 - Ir ao Hospital de Pokemons")
        print("0 - Sair do jogo")
        escolha = input("Sua escolha: ")

        if escolha == "1":
            player.explorar()
            salvar_jogo(player)
        elif escolha == "2":
            iminigo_aleatorio = Inimigo()
            player.batalhar(iminigo_aleatorio)
            salvar_jogo(player)
        elif escolha == "3":
            player.pokeagenda()
        elif escolha == "4":
            player.poke_hospital()
            salvar_jogo(player)
        elif escolha == "0":
            print("Finalizando o jogo..")
            break
        else:
            print("Escolha errada.")




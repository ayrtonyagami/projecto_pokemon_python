import random
from Pokemon import *


NOMES = [
    "Kira", "Toy", "Anderson","Bernado",
    "Violeta", "Elsa", "Alice","Adele","Helena",
    "Yagam-T", "Ariclene", "Antonio", "Victor",
    "Paulina","Isa","Rosa","Maria","Ash",
    "Misty","Brock","Jessie","James","Giselle",
    "Joe"
]

POKEMONS_Random = [
    PokemonFogo("Charmander"),
    PokemonFogo("Botafogo"),
    PokemonFogo("Charizard"),
    PokemonElectrico("Pikachu"),
    PokemonElectrico("Pokethor"),
    PokemonElectrico("Raichu"),
    PokemonAgua("Bolha-chin"),
    PokemonAgua("Curvina"),
    PokemonAgua("Flarion"),
    PokemonAgua("Slowpoke"),
    PokemonPlanta("Bulbace"),
    PokemonPlanta("Oddace"),
    PokemonPlanta("Sproutace"),
    PokemonInsecto("batterfree"),
    PokemonVoador("Pidgeot")
]



class Pessoa:
    def __init__(self,nome=None,pokemons=[], dinheiro = 100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        
        self.pokemons = pokemons
        self.dinheiro = dinheiro

    def __str__(self) -> str:
        return self.nome
    
    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for index, pk in enumerate(self.pokemons):
                print("{} - {}".format(index,pk))
            print()
        else:
            print(">>> {} está sem pokemons (┬┬﹏┬┬) ".format(self))

    def mostrar_dinheiro(self):
        print("Você em ${} na conta".format(self.dinheiro))
    
    def ganhar_dinheiro(self, dinheiro):
        self.dinheiro += dinheiro
        print("Ganhou ${}".format(dinheiro))
        self.mostrar_dinheiro()

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}.".format(self,pessoa))
        pessoa.mostrar_pokemons()
        pokemon_iminigo = pessoa.escolher_pokemons()
        pokemon = self.escolher_pokemons()

        if pokemon and pokemon_iminigo:
            
            while True:
                venceu = pokemon.atacar(pokemon_iminigo)
                input()
                if venceu:
                    print("{} VENCEU A BATALHA !!!".format(self))
                    self.ganhar_dinheiro(pokemon_iminigo.level * 25)
                    break      

                inimigo_venceu = pokemon_iminigo.atacar(pokemon)
                input()
                if inimigo_venceu:
                    print("{} VENCEU A BATALHA !!!".format(pessoa))
                    break
        else:
            print("Essa batalha não pode ocorrer!")
    
    def escolher_pokemons(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(self.nome, " escolheu {}!!!".format(pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("Erro: Esse jogador não tem nenhum pokemon.")


class Player(Pessoa):
    tipo = "player"

    def capturar(self,pokemon):
        self.pokemons.append(pokemon)
        print(">>>> {} capturou {}, parabens! o(*^▽^*)┛".format(self,pokemon))


    def escolher_pokemons(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha o seu pokemon ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print(pokemon_escolhido, "eu escolho vecê!!!")
                    return pokemon_escolhido
                except:
                    print("Escolha inválida")
        else:
            print("Erro: Esse jogador não tem nenhum pokemon.")

    def explorar(self):
        if random.random() >= 0.3:
            pokemon = random.choice(POKEMONS_Random)
            print("Apareceu um pokemon salvagem: {}".format(pokemon))

            escolha = input("Deseja capturar esse pokemon? (s/n)")
            if escolha == "s" or escolha == "sim":
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print("Que pena, esse pokemon fugio!")
            else:
                print("Ok.. podes contunuar a tua exploração..")
        else:
            print(">>>> Nenhum pokemon foi encontrado.")

    def pokeagenda(self):
        print("====================================")
        print("===          POKE-AGENDA          ==")
        print("====================================")
        while True:
            self.mostrar_pokemons()
            print("< - Fechar poke-agenda")
            escolha = input("Sua escolha: ")
            try:
                if escolha == "<" or escolha == "sair":
                    break
                else:
                    pokemon_escolhido = self.pokemons[int(escolha)]
                    pokemon_escolhido.info()
            except:
                print("Escolha errada!")

    def poke_hospital(self):
        print("====================================")
        print("===    HOSPITAL DE POKEMONS       ==")
        print("====================================")
        while True:
            self.mostrar_pokemons()
            print("< - Fechar poke-agenda")
            escolha = input("Sua escolha: ")
            try:
                if escolha == "<" or escolha == "sair":
                    break
                else:
                    if self.dinheiro >= 50:
                        pokemon_escolhido = self.pokemons[int(escolha)]
                        pokemon_escolhido.curar()
                        self.dinheiro -=50
                    else:
                        self.mostrar_dinheiro()
                        print("Você não tem dinheiro suficiente para curar o teu pokemon")
                        input("Você deve ter no mínimo $50.")

            except:
                print("Escolha errada!")

class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_inimigo = []
            for i in range(random.randint(1,4)):
                pokemons_inimigo.append(random.choice(POKEMONS_Random))

            super().__init__(nome, pokemons=pokemons_inimigo)
        else:
            super().__init__(nome, pokemons)







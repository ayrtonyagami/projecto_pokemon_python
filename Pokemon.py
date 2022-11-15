import random

class Pokemon:

    #construtor da class
    def __init__(self,especie,level=None, nome=None):
        self.especie = especie

        if level:
            self.level= level
        else:
            self.level = random.randint(1,4)

        self.vida = 50 + (self.level*50)
        self.poder_de_ataque = self.level*10

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    
    #o toString
    def __str__(self):
        return "{}({})".format(self.nome,self.level)
    
    def atacar(self, pokemon):
        vida_perdida = int(self.poder_de_ataque * random.random() * 1.3)
        pokemon.vida = pokemon.vida - vida_perdida

        if vida_perdida == 0:
            print(">>>> {} consegui esquivar-se do ataque!!".format(pokemon))
        else:
            print(">>>> {} perdeu {} pontos de vidas e ficou com {} vidas".format(pokemon.nome, vida_perdida,pokemon.vida))

        if pokemon.vida <= 0:
            print("{} derrotou {}".format(self,pokemon))
            return True
        else:
            return False
    
    def info(self):
        print("=====================")
        print("== Nome: {}".format(self.nome))
        print("== Tipo: {}".format(self.tipo))
        print("== Especie: {}".format(self.especie))
        print("== Level: {}".format(self.level))
        print("== Vida: {}".format(self.vida))
        print("== Poder de ataque: {}".format(self.poder_de_ataque))
        print("=====================")

    def curar(self):
        self.vida = 50 + (self.level*50)
        print("{} tem {} vidas".format(self,self.vida))


class PokemonElectrico(Pokemon):
    tipo = "Eletrico"

    def atacar(self, pokemon):
        print(">>>> {} lançou um raio do trovão em {}".format(self,pokemon))
        return super().atacar(pokemon)


class PokemonFogo(Pokemon):
    tipo = "Fogo"

    def atacar(self, pokemon):
        print(">>>> {} lançou uma bola de fogo na cabeça de {}".format(self,pokemon))
        return super().atacar(pokemon)


class PokemonAgua(Pokemon):
    tipo = "Água"

    def atacar(self, pokemon):
        print(">>>> {} lançou um jato de água em {}".format(self,pokemon))
        return super().atacar(pokemon)


class PokemonPlanta(Pokemon):
    tipo = "Planta"

    def atacar(self, pokemon):
        print(">>>> {} lançou folhas cortante em {}".format(self,pokemon))
        return super().atacar(pokemon)


class PokemonInsecto(Pokemon):
    tipo = "Insecto"

    def atacar(self, pokemon):
        print(">>>> {} lançou folhas cortante em {}".format(self,pokemon))
        return super().atacar(pokemon)

class PokemonPsquico(Pokemon):
    tipo = "Psquico"

    def atacar(self, pokemon):
        print(">>>> {} lançou poder de confusão mental em {}".format(self,pokemon))
        return super().atacar(pokemon)
    

class PokemonVoador(Pokemon):
    tipo = "Voador"

    def atacar(self, pokemon):
        print(">>>> {} lançou ragada de vento em {}".format(self,pokemon))
        return super().atacar(pokemon)
    




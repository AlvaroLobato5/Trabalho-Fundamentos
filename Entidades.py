from random import randint


def variables_checker(tipo, minimo, maximo):
    def decorator(func):
        def inner(self, valor):

            if type(valor) != tipo:
                tipo_str = str(tipo).replace('<class \'', '').replace('\'>', '')
                raise TypeError(f'Valor deve ser um {tipo_str}.')

            if minimo < valor <= maximo:
                func(self, valor)
            else:
                raise ValueError(f'Valor deve estar entre {minimo} e {maximo}')

        return inner

    return decorator


class Entidade:
    def __init__(self, vida_maxima, crit_chance=2.0):
        self.__alive = True
        self.__vida_maxima = vida_maxima
        self.__vida = vida_maxima
        self.__attack_damage = 1
        self.__crit_chance = crit_chance

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        self.__vida = min(valor, self.__vida_maxima)

    @property
    def alive(self):
        return self.__alive

    @property
    def vida_maxima(self):
        return self.__vida_maxima

    @vida_maxima.setter
    @variables_checker(int, 0, 30)
    def vida_maxima(self, valor):
        self.__vida_maxima = valor

    def add_vida_maxima(self, valor):
        self.vida_maxima += valor
        self.vida += valor

    @property
    def attack_damage(self):
        return self.__attack_damage

    @attack_damage.setter
    def attack_damage(self, valor):
        if type(valor) != int:
            raise TypeError('Valor deve ser um inteiro.')
        if 0 < valor <= 5:
            self.__attack_damage = valor
        else:
            raise ValueError('Valor deve estar entre 1 e 5')

    @property
    def crit_chance(self):
        return self.__attack_damage

    @crit_chance.setter
    @variables_checker(float, 0, 10)
    def crit_chance(self, valor):
        self.__crit_chance = valor

    def damage(self, dmg, dmg_source=None):
        self.vida -= dmg
        if self.vida <= 0:
            self.die()
            return

    def attack(self, alvo):
        crit = randint(1, 10) <= self.__crit_chance
        if crit:
            alvo.damage(self.__attack_damage*2, dmg_source=self)
        else:
            alvo.damage(self.__attack_damage, dmg_source=self)

    def die(self):
        self.__alive = False
        print('Morto')

    def curar(self, quantidade):
        self.vida = min(self.__vida_maxima, self.__vida+quantidade)


class Monstro(Entidade):
    def damage(self, dmg, dmg_source=None):
        super().damage(dmg, dmg_source)
        if dmg_source is not None:
            if randint(0, 9) <= 7:
                self.attack(dmg_source)


class Jogador(Entidade):
    def __init__(self, vida_maxima):
        super().__init__(vida_maxima)
        self.veneno = False
        self.tempo_veneno = 0
        self.x = 0
        self.y = 0
        self.inventario = {}
        self.sala_atual = None
        self.em_combate = False
        self.combate_menu = None
        self.main_menu = None
        self.arma_equipada = None
        self.mapa_descoberto = [['* ' for _ in range(5)] for _ in range(5)]

    def damage(self, dmg, dmg_source=None):
        super().damage(dmg, dmg_source)
        print(f'Você tomou {dmg} de dano de {dmg_source}')
        if self.vida <= 0:
            self.die()

    def adicionar_inventario(self, item: str, quantidade: int):
        try:
            self.inventario[item] += quantidade
        except KeyError:
            self.inventario[item] = quantidade

    def exibir_inventario(self):
        print('-'*20+'\n')
        if self.inventario == {}:
            print('Inventário vazio')
        for k, v in self.inventario.items():
            print(f'{k}: {v}')
        print('\n'+'-'*20)

        if 'espada' in self.inventario.items():
            res = input('Deseja equipar a espada? (s/N)')
            if res.lower() in ['s', 'sim']:
                print(self.equipar_arma('espada'))
        elif 'adaga' in self.inventario.items():
            res = input('Deseja equipar a adaga? (s/N)')
            if res.lower() in ['s', 'sim']:
                print(self.equipar_arma('adaga'))

    def exibir_atributos(self):
        print('-'*20+'\n')
        print(f'Vida: {self.vida}/{self.vida_maxima}')
        print(f'Dano de ataque: {self.attack_damage}')
        print(f'Chance de crítico: {self.crit_chance*10}%')
        print('\n'+'-'*20)

    def equipar_arma(self, arma):
        self.arma_equipada = arma
        self.__attack_damage += 1
        return 'Arma equipada com sucesso'

    def andar(self, direcao: str):
        self.mapa_descoberto[self.y][self.x] = str(self.sala_atual) + ' '
        if direcao.lower() == 'norte':
            if self.y == 0:
                print('Movimento Inválido')
                return False
            self.y -= 1
        elif direcao.lower() == 'sul':
            if self.y == 4:
                print('Movimento Inválido')
                return False
            self.y += 1
        elif direcao.lower() == 'leste':
            if self.x == '4':
                print('Movimento Inválido')
                return False
            self.x += 1
        elif direcao.lower() == 'oeste':
            if self.x == 0:
                print('Movimento Inválido')
                return False
            self.x -= 1

        return True

    def tick_veneno(self):
        if self.tempo_veneno > 0:
            self.damage(1, 'veneno')
            self.tempo_veneno -= 1

    def die(self):
        print('Você morreu.')
        quit()

    def __str__(self):
        return 'Jogador'


class Cozinheiro(Monstro):
    def __init__(self):
        super().__init__(15, crit_chance=2.0)
        self.attack_damage = 1

    def __str__(self):
        return 'Cozinheiro'
    

class Quimera(Monstro):
    def __init__(self):
        super().__init__(20)
        self.attack_damage = 2
        self.__veneno_tempo = 3
        self.crit_chance = 4.0

    def attack(self, alvo):
        super().attack(alvo)
        if randint(1, 10) > 7:
            alvo.veneno = True
            alvo.tempo_veneno = self.__veneno_tempo

    def __str__(self):
        return 'Quimera'


class Carrasco(Monstro):
    def __init__(self):
        super().__init__(25)
        self.attack_damage = 1
        self.crit_chance = 7.0

    def __str__(self):
        return 'Carrasco'


class Mimico(Monstro):
    def drop(self):
        if not self.__alive:
            return 'Faca de cobre desgastada'

    def __str__(self):
        return 'Mímico'


if __name__ == '__main__':
    entidade = Entidade(10, 1)
    entidade.vida_maxima = 200

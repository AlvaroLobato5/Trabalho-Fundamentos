import os
import Menu


class Desafio:
    def __init__(self):
        self.resolvido = False


class Quiz(Desafio):
    def __init__(self, respostas: tuple, texto: str = '', textos: tuple = ()):

        super().__init__()
        if textos:
            self.textos = textos
        else:
            self.textos = (texto, )

        self.respostas = respostas

    def iniciar(self):
        if self.resolvido:
            return
        for i in range(len(self.textos)):
            res = input(self.textos[i])
            if res.lower() in self.respostas:
                print('Parabéns!')
                self.resolvido = True
                return True
        else:
            print('Você errou!')
            return False


class Command(Desafio):
    def __init__(self, texto: str, args):
        super().__init__()
        self.texto = texto
        self.args = args

    def iniciar(self):
        if self.resolvido:
            return
        print(self.texto)
        os.system(self.args)


class Combate(Desafio):
    def __init__(self, jogador, alvo):
        super().__init__()
        self.jogador = jogador
        self.alvo = alvo

    def iniciar(self):
        if self.resolvido:
            return
        self.jogador.combate_menu.alvo = self.alvo
        self.jogador.em_combate = True
        self.jogador.combate_menu.prompt()
        self.jogador.em_combate = False
        self.resolvido = True
        return True


if __name__ == '__main__':
    Quiz(respostas=('a', ), textos=(1, 2)).iniciar()
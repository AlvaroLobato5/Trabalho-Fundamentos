from Mapa import Mapa
from Entidades import Jogador
from Menu import MainMenu, CombateMenu
from time import sleep


def main():
    jogador = Jogador(vida_maxima=10)
    mapa = Mapa(jogador)
    jogador.main_menu = MainMenu(mapa)
    jogador.combate_menu = CombateMenu(jogador, None)
    while True:
        jogador.tick_veneno()
        jogador.main_menu.prompt()
        sleep(1)


if __name__ == '__main__':
    main()

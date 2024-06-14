from Mapa import Mapa
from Entidades import Jogador
from Menu import MainMenu, CombateMenu


def main():
    jogador = Jogador(vida_maxima=30)
    mapa = Mapa(jogador)
    jogador.main_menu = MainMenu(mapa)
    jogador.combate_menu = CombateMenu(jogador, None)
    while True:
        jogador.tick_veneno()
        jogador.main_menu.prompt()


if __name__ == '__main__':
    main()

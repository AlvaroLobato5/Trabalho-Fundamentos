from Mapa import Mapa
from Entidades import Jogador
from Menu import MainMenu, CombateMenu


# TODO: Add visualizador stats
# TODO: Add mensagens pos conclusao de salas falando qual a recompensa

def main():
    jogador = Jogador(vida_maxima=150)
    mapa = Mapa(jogador)
    jogador.main_menu = MainMenu(mapa)
    jogador.combate_menu = CombateMenu(jogador, None)
    while True:
        jogador.tick_veneno()
        jogador.main_menu.prompt()


if __name__ == '__main__':
    main()

from Jogo.Mapa import Mapa
from Jogo.Entidades import Jogador
from Jogo.Menu import MainMenu, CombateMenu
from time import sleep


def main():
    jogador = Jogador(vida_maxima=10)
    mapa = Mapa(jogador=jogador)
    mapa.mover_jogador(0, 0)
    jogador.main_menu = MainMenu(mapa)
    jogador.combate_menu = CombateMenu(jogador, None)
    while jogador.alive:
        jogador.tick_veneno()
        jogador.main_menu.prompt()
        sleep(0.5)

    input('Você morreu...\nAperte Enter para sair.')


if __name__ == '__main__':
    main()

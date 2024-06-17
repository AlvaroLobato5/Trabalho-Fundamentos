class MainMenu:
    def __init__(self, mapa):
        self.mapa = mapa
        self.jogador = self.mapa.jogador

    def exibir_player_mapa(self):
        print('-' * 20 + '\n')
        print(f'Vida: {self.jogador.vida}/{self.jogador.vida_maxima}\n')
        print('Mapa:')
        for i in range(5):
            for j in range(5):
                if i == self.jogador.y and j == self.jogador.x:
                    print('P ', end='')
                else:
                    print(str(self.jogador.mapa_descoberto[i][j])+' ', end='')
            print()

        print('\n' + '-' * 20)

    def prompt(self):
        self.exibir_player_mapa()

        opcao = input('O que você deseja fazer?'
                      '\n1. Se movimentar'
                      f'\n2. Interagir com a sala ({self.jogador.sala_atual})'
                      f'\n3. Descrever o ambiente'
                      '\n4. Verificar inventário'
                      '\n5. Ver atributos'
                      '\n6. Sair do jogo'
                      '\n')
        if opcao == '1':

            direcao = input('Deseja se mover para qual direção?'
                            '\n1. Norte'
                            '\n2. Sul'
                            '\n3. Leste'
                            '\n4. Oeste'
                            '\n')
            if self.jogador.andar(direcao):
                self.mapa.mover_jogador(self.jogador.x, self.jogador.y)

        elif opcao == '2':
            self.jogador.sala_atual.interagir(jogador=self.jogador, mapa=self.mapa.matriz)
        elif opcao == '3':
            self.jogador.sala_atual.descrever()
        elif opcao == '4':
            self.jogador.exibir_inventario()
        elif opcao == '5':
            self.jogador.exibir_atributos()
        elif opcao == '6':
            print('Tchau!')
            quit()


class CombateMenu:
    def __init__(self, jogador, alvo):
        self.jogador = jogador
        self.alvo = alvo

    def prompt(self):
        print(f'Você entrou em um combate com o {self.alvo}.')
        while self.alvo.alive and self.jogador.alive:
            print(f'{self.alvo}: {self.alvo.vida}/{self.alvo.vida_maxima}')
            print(f'{self.jogador}: {self.jogador.vida}/{self.jogador.vida_maxima}')

            acao = input('\n1. Atacar'
                         '\n2. Defender')

            if acao.lower() in ['1', 'atacar']:
                self.alvo.damage(self.jogador.attack_damage, self.jogador)
            elif acao.lower() in ['2', 'defender']:
                print(f'Você defendeu um ataque do {self.alvo}.')

            self.jogador.tick_veneno()

import Salas
import Desafios
import Entidades


# Sala Tesouro Falsa:
# Combate mímico

# Passagem Secreta:
# Resolver desafio e mandar direto pro Tesouro
# Rolar um dado, se tirar 6 vai para a sala do Tesouro

# Salão de Festas:
# Tem um colar de joias, uma cartola e uma espada
# No salão de festas tem um cavaleiro, uma donzela e um nobre, com qual item cada um deles deve ficar?

# Quarto de Hóspedes:
# No quarto de Hóspedes pode descansar e regenerar toda vida


class Mapa:
    def __init__(self, jogador):
        self.__jogador = jogador
        self.__matriz = [
            [Salas.Entrada(),
             Salas.Corredor(Desafios.Quiz(texto='Qual o nome da bijuu selada dentro do corpo de Naruto durante o anime '
                                          'Naruto?', respostas=('kurama', ))),
             Salas.SalaArmas(Desafios.Command(texto='Seu computador irá desligar em 60 segundos.'
                                              '\nVocê tem esse tempo para cancelar o comando.',
                                        args="shutdown /s /t 60")),
             Salas.Biblioteca(Desafios.Quiz(texto='Sou leve como uma pena, mas nem a pessoa mais forte do mundo '
                                        'consegue me segurar por mais de cinco minutos. O que sou?',
                                      respostas=('a respiração', 'respiração'))),
            'Tesouro'],
            [Salas.Cozinha(Desafios.Combate(jogador=self.jogador, alvo=Entidades.Cozinheiro())),
             Salas.SalaJantar(Desafios.Quiz(texto='Em frente, há uma verdura de folhas largas e onduladas, com um verde vibrante e bordas ligeiramente serrilhadas.'
                                                  '\nA textura é crocante e refrescante, e as folhas parecem quase brilhosas sob a luz.'
                                                  '\nEsta verdura é frequentemente usada em saladas por seu sabor leve e agradável.'
                                                  '\nQual é essa verdura?', respostas=('a alface', 'alface'))),
            Salas.Calabouco(Desafios.Combate(jogador=self.__jogador, alvo=Entidades.Carrasco())),
             Salas.SalaMusica(Desafios.Quiz(texto='Quantas sinfonias Mozart tem?', respostas=('41', 'quarenta e um'))),
             Salas.AposentosRei(Desafios.Dado())],
            ['Jardim', 'Pátio',
             Salas.Estabulo(Desafios.Quiz(texto='Dado os seguintes animais e alimentos, associe cada alimento ao animal correto, respectivamente. '
                                '\nAnimais: Leão, Coelho, Panda'
                                '\nAlimentos: Cenouras, Bambu, Antílopes'
                                '\nPadrão de resposta Animal1 - Alimento1, Animal2 - Alimento2, Animal3 - Alimento3'
                                '\nEspaços são consideradas, usar a vírgula para separar as respstas\n',
                                respostas=('leão - antílopes, coelho - cenouras, panda - bambu', ))),
             Salas.Capela(Desafios.Quiz(texto="Coloque os livros da Bíblia em ordem cronológica: Josué, Êxodo, Juízes e Esdras\nEx: 1 Samuel - 2 Samuel - 1 Reis - 2 Reis (Use espaços)",
                                        respostas=('êxodo - josué - juízes - esdras', ))), 'Salão de Festas'],
            [Salas.Torre(Desafios.Quiz(texto='\nAtravés do telescópio, avista-se três criaturas de aparência furtiva e desgrenhada, movendo-se cautelosamente entre as árvores retorcidas da floresta.'
                                              '\nSuas peles verdes e manchadas contrastam com o ambiente sombrio ao redor, e elas parecem estar em constante vigilância, examinando o terreno com olhos astutos.'
                                              '\nArmadas com lanças rudimentares e vestindo trapos improvisados, elas se comunicam em grunhidos guturais enquanto desaparecem rapidamente entre as sombras, deixando uma sensação de intriga e perigo iminente.'
                                              '\nQue criaturas misteriosas são essas?\n',
                                       respostas=('goblin', 'goblins'))),
             Salas.Laboratorio(Desafios.Combate(jogador=self.jogador, alvo=Entidades.Quimera())),
             Salas.SalaMago(Desafios.Quiz(texto='Utilize 2 das 9 palavras abaixo para criar um feitiço de luz em área: \nlux, area, ignis, verba, noctem, vita, lupum',
                                          respostas=('area lux',))),
             Salas.GaleriaDeArte(Desafios.Quiz(textos=
                                               ('Esta pintura, criada em 1889, retrata um céu noturno turbulento com vórtices celestes e uma lua crescente sobre um vilarejo adormecido. Qual é o nome dessa obra famosa?',
                                                'Esta obra icônica foi pintada pelo artista holandês Vincent van Gogh enquanto ele estava internado em um asilo em Saint-Rémy-de-Provence. Como se chama essa pintura?',
                                                'Considerada uma das mais conhecidas obras de arte do pós-impressionismo, esta pintura de Vincent van Gogh é conhecida por seu céu agitado e estrelado. Qual é o nome desta obra?'),
                                               respostas=('a noite estrelada', 'noite estrelada'))),
             Salas.SalaTrono(Desafios.Quiz(texto='O que é que de manhã tem quatro patas, de tarde tem duas e de noite tem três?', respostas=('o ser humano', 'ser humano')))],
            [Salas.SalaGuardas(Desafios.Quiz(
                texto='Você se depara com dois guardas na frente de duas portas. Um dos guardas sempre mente, e o outro sempre diz a verdade.'
                      ' Uma das portas leva à liberdade, enquanto a outra leva à morte.'
                      ' Você pode fazer apenas uma pergunta para um dos guardas para descobrir qual porta é a correta. Qual pergunta você faz?'
                      '\n 1. Você está guardando a porta da liberdade?'
                      '\n 2. Se eu perguntasse ao outro guarda qual porta leva à liberdade, o que ele me diria?'
                      '\n 3. Qual porta você guarda?'
                      '\n 4. A outra porta leva à morte?'
                      '\n 5. A porta à sua esquerda leva à liberdade?\n',
                respostas=('2', 'se eu perguntasse ao outro guarda qual porta leva à liberdade, o que ele me diria?'))),
                Salas.Corredor(Desafios.Quiz(texto='Qual o nome do Pai de Naruto?',
                                             respostas=('minato namikaze', 'namikaze minato'))), 'Sala Tesouro Falsa',
             'Passagem secreta', 'Quarto Hóspedes']
        ]

        self.jogador.sala_atual = self.matriz[0][0]

    @property
    def matriz(self):
        return self.__matriz

    @property
    def jogador(self):
        return self.__jogador

    def mover_jogador(self, x, y):
        self.jogador.sala_atual = self.matriz[y][x]
        try:
            self.jogador.sala_atual.entrar()
        except AttributeError:
            pass

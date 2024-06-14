import Salas
import Desafios
import Entidades

# Sala do Mago:
# Dar 7 palavras e preciso fazer uma magia que ilumine uma grande área e combine 2 palavras em latim
# lux, area, ignis, verba, noctem, vita, lupum
# Area lux


# Sala de Jantar:
# Você tem um prato de salada na sua frente, descrever uma verdura e perguntar qual é

# Calabouço:
# Matar o Carrasco

# Sala de Música:
# Quantas sinfonias Mozart tem
# 41

# Aposentos Rei:
# RNG de D6, pra roubar a coroa

# Torre:
# Você está vendo por um telescópio a silhueta de 3 criaturas.
# Descrever goblins e a resposta é goblin

# Sala do Trono:
# Se tiver roubado a coroa, vai ser pego pelos guardas
# Desafio/Enigma:
# O que é que de manhã tem quatro patas, de tarde tem duas e de noite tem três? O ser humano.

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
            [Salas.Cozinha(Desafios.Combate(jogador=self.jogador, alvo=Entidades.Cozinheiro())), 'Sala de Jantar', 'Calabouço', 'Sala de Música', 'Aposentos Rei'],
            ['Jardim', 'Pátio', Salas.Estabulo(
                Desafios.Quiz(texto='Dado os seguintes animais e alimentos, associe cada alimento ao animal correto, respectivamente. '
                                '\nAnimais: Leão, Coelho, Panda'
                                '\nAlimentos: Cenouras, Bambu, Antílopes'
                                '\nPadrão de resposta Animal1 - Alimento1, Animal2 - Alimento2, Animal3 - Alimento3'
                                '\nEspaços são consideradas, usar a vírgula para separar as respstas\n',
                                respostas=('leão - antílopes, coelho - cenouras, panda - bambu', ))),
             Salas.Capela(Desafios.Quiz(texto="Coloque os livros da Bíblia em ordem cronológica: Josué, Êxodo, Juízes e Esdras\nEx: 1 Samuel - 2 Samuel - 1 Reis - 2 Reis (Use espaços)",
                                        respostas=('êxodo - josué - juízes - esdras', ))), 'Salão de Festas'],
            ['Torre', Salas.Laboratorio(Desafios.Combate(jogador=self.jogador, alvo=Entidades.Quimera())),
             Salas.SalaMago(Desafios.Quiz(texto='Utilize 2 das 9 palavras abaixo para criar um feitiço de luz em área: \nlux, area, ignis, verba, noctem, vita, lupum',
                                          respostas=('area lux',))),
             Salas.GaleriaDeArte(Desafios.Quiz(textos=
                                               ('Esta pintura, criada em 1889, retrata um céu noturno turbulento com vórtices celestes e uma lua crescente sobre um vilarejo adormecido. Qual é o nome dessa obra famosa?',
                                                'Esta obra icônica foi pintada pelo artista holandês Vincent van Gogh enquanto ele estava internado em um asilo em Saint-Rémy-de-Provence. Como se chama essa pintura?',
                                                'Considerada uma das mais conhecidas obras de arte do pós-impressionismo, esta pintura de Vincent van Gogh é conhecida por seu céu agitado e estrelado. Qual é o nome desta obra?'),
                                               respostas=('a noite estrelada', 'noite estrelada'))), 'Sala do Trono'],
            [Salas.SalaGuardas(Desafios.Quiz(
                texto='Você se depara com dois guardas na frente de duas portas. Um dos guardas sempre mente, e o outro sempre diz a verdade.'
                      ' Uma das portas leva à liberdade, enquanto a outra leva à morte.'
                      ' Você pode fazer apenas uma pergunta para um dos guardas para descobrir qual porta é a correta. Qual pergunta você faz?'
                      '\n 1. Você está guardando a porta da liberdade?'
                      '\n 2. Se eu perguntasse ao outro guarda qual porta leva à liberdade, o que ele me diria?'
                      '\n 3. Qual porta você guarda?'
                      '\n 4. A outra porta leva à morte?'
                      '\n 5. A porta à sua esquerda leva à liberdade?\n',
                respostas=('2', 'se eu perguntasse ao outro guarda qual porta leva à liberdade, o que ele me diria?'))), Salas.Corredor(Desafios.Quiz(texto='Qual o nome do Pai de Naruto?',
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

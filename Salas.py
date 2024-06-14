from random import randint


class Sala:
    def __init__(self, desafio):
        self.desafio = desafio

    @staticmethod
    def descrever():
        print('\nSala vazia\n')

    def __str__(self):
        return 'Sala'


class Entrada(Sala):
    def __init__(self):
        super().__init__(None)

    def entrar(self):
        print('Você está na entrada!')
        interagir_guardas = input('Você encontrou 2 guardas na porta, deseja interagir com eles? (S/N)')
        if interagir_guardas == 'S':
            print('Você foi ignorado.')

    @staticmethod
    def descrever():
        print('\nA Sala do Guardião se revela como um espaço compacto e silencioso, com paredes de pedra iluminadas por tochas bruxuleantes. '
                '\nNo centro, um intrincado mecanismo de madeira e ferro domina a sala, claramente destinado a controlar a portcullis suspensa acima. '
                '\nCorrentes robustas e engrenagens são visíveis, prontas para ação. O ambiente é marcado pela ausência de guardas, mas a sensação de vigilância persiste, transmitida pelos detalhes funcionais do espaço.'
                '\nArmaduras e armas estão organizadas meticulosamente, reforçando a atmosfera de prontidão e defesa implacável.\n')

    def interagir(self, **kwargs):
        opcao = input('Você encontrou um baú'
                      '\nDeseja roubar? (s/N)'
                      '\n')

        if opcao.lower() in ['s', 'sim']:
            print('Os guardas te pegaram.')
            quit()
        else:
            print('Nada aconteceu.')

    def __str__(self):
        return 'Entrada'


class Corredor(Sala):
    def entrar(self):
        print('Você está no corredor')

    @staticmethod
    def descrever():
        print('\nO corredor do castelo se estende à frente, com paredes de pedra maciça que refletem a luz suave das tochas alinhadas em intervalos regulares.'
                '\nO chão é coberto por lajes de pedra desgastadas pelo tempo, emitindo um leve eco a cada passo.'
                '\nTapeçarias ricas e detalhadas adornam as paredes, retratando cenas de batalhas e caçadas, trazendo um toque de cor e história ao ambiente austero.'
                '\nPortas de madeira reforçada, algumas entreabertas, revelam vislumbres de outros quartos e câmaras.'
                '\nO ar é fresco, com uma leve corrente que atravessa o corredor, carregando o sutil cheiro de cera de vela e pedra fria.'
                '\nA atmosfera é solene e tranquila, com uma sensação palpável de segurança e antiguidade.\n')

    def __str__(self):
        return 'Corredor'


class SalaArmas(Sala):
    def __init__(self, desafio):
        self.itens = ['espada', 'adaga']
        super().__init__(desafio)

    @staticmethod
    def descrever():
        print('\nA sala de armas do castelo é um espaço impressionante, com paredes revestidas de madeira escura e ricamente adornadas com armamentos.'
                '\nEspadas, lanças, machados e escudos estão organizados em suportes meticulosos, cada um exibindo sinais de uso e história.'
                '\nArmaduras completas, algumas decoradas com brasões e insígnias, estão dispostas em pedestais ao longo das paredes.'
                '\nNo centro da sala, uma grande mesa de madeira exibe mapas e táticas de batalha, iluminada pela luz suave das tochas que pendem das paredes.'
                '\nO ar é impregnado com o cheiro de óleo de manutenção e metal polido, criando uma atmosfera de prontidão e tradição militar.'
                '\nCada detalhe da sala evoca a sensação de preparação constante e respeito pelas artes da guerra.\n')

    def entrar(self):
        print('Você entrou em uma sala cheia de armas.')

    def interagir(self, **kwargs):
        opcao = input('Deseja roubar? (s/N)')
        if opcao == 'S':
            concluido = self.desafio.iniciar()
            if concluido:
                kwargs.get('jogador').adicionar_inventario(self.itens[randint(0, 1)], 1)
            elif concluido is None:
                print('Essa sala já foi roubada.')
            elif not concluido:
                print('Você falhou!')

    def __str__(self):
        return 'Sala de Armas'


class Biblioteca(Sala):
    def entrar(self):
        print('Você encontrou uma biblioteca abandonada.')

    def interagir(self, **kwargs):
        if self.desafio.iniciar():
            print('Parabéns, você acertou.')
            print('O tesouro está a 1 casa de distância de você.')

    @staticmethod
    def descrever():
        print('\nA biblioteca do castelo é um refúgio de conhecimento e tranquilidade.'
                '\nParedes altas são revestidas com estantes de madeira escura, repletas de livros encadernados em couro, manuscritos antigos e pergaminhos preciosos.'
                '\nUma grande mesa central, coberta por veludo verde, está repleta de livros abertos, penas e tinteiros, evidenciando um local de estudo ativo.'
                '\nCandelabros de ferro forjado pendem do teto abobadado, lançando uma luz suave e cálida que dança nas lombadas dos livros.'
                '\nGrandes janelas com vitrais coloridos permitem a entrada de luz natural, criando um jogo de sombras e cores no chão de pedra.'
                '\nPoltronas confortáveis e estofadas estão dispostas em cantos estratégicos, convidando à leitura e reflexão.'
                '\nO ar é impregnado com o cheiro de papel envelhecido e couro, imbuindo a sala com uma sensação de história e erudição.'
                '\nA atmosfera é de reverência e quietude, um santuário de saber em meio à fortaleza imponente.\n')

    def __str__(self):
        return 'Biblioteca'


class Cozinha(Sala):
    def entrar(self):
        print('Você entrou na cozinha.')

    def interagir(self, **kwargs):
        opcao = input('Tentar roubar comida da cozinha? (s/N)')
        if opcao.lower() in ['s', 'Sim']:
            concluido = self.desafio.iniciar()
            if concluido:
                kwargs.get('jogador').curar(10)
            elif concluido is None:
                print('Cozinha já roubada.')

    @staticmethod
    def descrever():
        print('\nNa cozinha do castelo, um ambiente que mistura calor e atividade fervilhante, há um cozinheiro de estatura imponente conhecido apenas como Grunk.'
                '\nCom seus braços robustos e mãos ágeis, Grunk move-se entre os caldeirões borbulhantes e os fogões a lenha com uma destreza surpreendente para alguém de seu tamanho.'
                '\nEle comanda a cozinha com uma voz trovejante, coordenando a equipe de ajudantes e cozinheiros menores com autoridade e eficiência.'
                '\nSeu avental de couro está manchado de gordura e temperos, e seu rosto largo e barbudo exibe uma expressão concentrada enquanto prova, ajusta e tempera os pratos que estão em preparação.'
                '\nEnquanto os assistentes correm de um lado para o outro, Grunk supervisiona pessoalmente cada etapa, garantindo que cada refeição seja preparada com perfeição para satisfazer os exigentes paladares dos nobres e guerreiros que habitam o castelo.\n')

    def __str__(self):
        return 'Cozinha'


class GaleriaDeArte(Sala):
    def entrar(self):
        print('Você entrou na galeria de arte')

    def interagir(self, **kwargs):
        self.desafio.iniciar()

    def __str__(self):
        return 'Galeria de Arte'


class SalaGuardas(Sala):
    def entrar(self):
        print('Você entrou em uma sala com dois guardas.')

    @staticmethod
    def descrever():
        print('\nA galeria de arte do castelo é um tesouro de obras preciosas e históricas.'
                '\nParedes adornadas com tapeçarias antigas e vitrais coloridos criam um ambiente de beleza e elegância.'
                '\nEm cada canto, pedestais de mármore exibem esculturas intricadas e bustos de personalidades ilustres do passado.'
                '\nPinturas emolduradas em ouro e prata adornam as paredes, representando cenas de batalhas, retratos de nobres e paisagens pitorescas.'
                '\nUma atmosfera de tranquilidade permeia o espaço, apenas quebrada pelo sussurro dos visitantes enquanto admiram as obras de arte.'
                '\nLustres de cristal pendem do teto alto, refletindo a luz suave que banha as salas, destacando cada detalhe das obras expostas.'
                '\nO aroma de cera de abelha das velas perfumadas mistura-se com o cheiro sutil de madeira envelhecida, enchendo o ar com uma sensação de sofisticação e cultura refinada.'
                '\nA galeria é um testemunho do talento humano e do legado cultural que o castelo protege e celebra.\n')

    def interagir(self, **kwargs):
        concluido = self.desafio.iniciar()
        if concluido is None:
            pass
        elif not concluido:
            print('Você escolheu a porta errada!')
            quit()

    def __str__(self):
        return 'Sala de Guardas'


class Estabulo(Sala):
    def entrar(self):
        print('Você entrou no estábulo')

    def interagir(self, **kwargs):
        concluido = self.desafio.iniciar()
        if concluido is None:
            print('Você já alimentou os animais.')
        elif not concluido:
            print('Você errou a ordem dos alimentos.')
        else:
            print('O fazendeiro agradesce.')
            print('Você recebeu 3 de vida máxima')
            jogador = kwargs.get('jogador')
            jogador.vida_maxima += 3

    @staticmethod
    def descrever():
        print('\nO estábulo do castelo é um local de atividade constante e vitalidade.'
                '\nGrandes portas de madeira se abrem para revelar fileiras de baías, cada uma ocupada por cavalos de raças nobres e fortes, relinchando suavemente enquanto são acariciados pelos estábulos.'
                '\nA fragrância mista de feno fresco e grãos enche o ar, combinada com o cheiro reconfortante de couro e esterco.'
                '\nLuz natural entra pelas janelas altas, iluminando os espaços arejados onde os cavalariços habilidosos cuidam meticulosamente dos animais.'
                '\nO som de ferraduras batendo no chão de pedra ecoa pelo estábulo, criando uma sinfonia harmoniosa que complementa a energia vibrante do ambiente.'
                '\nFerramentas de equitação pendem das paredes de madeira, ao lado de escovas e baldes usados para a limpeza e manutenção diária dos cavalos.'
                '\nO estábulo é mais do que um lugar de abrigo para os animais; é um centro de cuidado e treinamento, essencial para a vida cotidiana e as operações do castelo medieval.\n')

    def __str__(self):
        return 'Estábulo'


class Laboratorio(Sala):
    def entrar(self):
        print('Você entrou no laboratório.')

    def interagir(self, **kwargs):
        opcao = input('Tentar roubar poção de dano? (s/N)')
        if opcao.lower() in ['s', 'Sim']:
            concluido = self.desafio.iniciar()
            if concluido:
                kwargs.get('jogador').attack_damage += 1
            elif concluido is None:
                print('Poção já roubada.')

    @staticmethod
    def descrever():
        print('\nO laboratório do castelo é um reduto de mistério e descoberta.'
                '\nParedes revestidas com prateleiras abrigam frascos de vidro contendo líquidos coloridos e poções borbulhantes, cada um cuidadosamente etiquetado com letras elaboradas.'
                '\nMesas de trabalho de madeira robusta estão espalhadas pelo espaço, cobertas por pergaminhos com fórmulas alquímicas e instrumentos de medição intricados.'
                '\nNo centro do laboratório, um grande alambique de cobre brilha à luz das velas, destilando essências aromáticas e ingredientes mágicos.'
                '\nO ar está impregnado com o aroma de ervas secas e produtos químicos, criando uma atmosfera de concentração e experimentação.'
                '\nJanelas altas permitem a entrada de luz natural, revelando uma miríade de cristais e minerais que adornam as prateleiras.'
                '\nAtrás de uma cortina pesada, uma estufa abriga plantas exóticas, cujas folhas e flores são colhidas para ingredientes de poções e remédios.'
                '\nO laboratório é um refúgio para o alquimista do castelo, onde segredos são descobertos e o conhecimento é ampliado em busca de poder e cura.\n')

    def __str__(self):
        return 'Laboratório'


class Capela(Sala):
    def entrar(self):
        print('Você entrou na capela')

    def interagir(self, **kwargs):
        self.desafio.iniciar()

    @staticmethod
    def descrever():
        print('\nA capela do castelo é um santuário de serenidade e espiritualidade.'
                '\nParedes altas de pedra são decoradas com vitrais coloridos que banham o espaço em uma luz divina, projetando padrões vibrantes no chão de pedra polida.'
                '\nUm altar de madeira esculpida se destaca no centro, adornado com velas queimando em castiçais de prata.'
                '\nBancos de madeira alinham-se em fileiras ordenadas, onde os fiéis se ajoelham em oração silenciosa.'
                '\nO aroma suave de incenso permeia o ar, evocando uma atmosfera de reverência e paz interior.'
                '\nPinturas sagradas adornam as paredes, retratando cenas religiosas e figuras veneradas pelos habitantes do castelo.'
                '\nUm órgão antigo repousa em um canto, seu som majestoso ocasionalmente preenchendo o espaço durante cerimônias e celebrações.'
                '\nA capela é um oásis espiritual dentro das robustas muralhas do castelo, onde a fé é cultivada e os corações encontram consolo e esperança.\n')

    def __str__(self):
        return 'Capela'


class SalaMago(Sala):
    
    def entrar(self):
        print('Você entrou na sala do mago')

    def interagir(self, **kwargs):
        jogador = kwargs.get('jogador')
        mapa = kwargs.get('mapa')
        concluido = self.desafio.iniciar()

        if concluido:
            print('O feitiço ilumina seu caminho e revela as salas ao seu redor')
            jogador.mapa_descoberto[jogador.y - 1][jogador.x] = mapa[jogador.y - 1][jogador.x]
            jogador.mapa_descoberto[jogador.y + 1][jogador.x] = mapa[jogador.y + 1][jogador.x]
            jogador.mapa_descoberto[jogador.y][jogador.x - 1] = mapa[jogador.y][jogador.x - 1]
            jogador.mapa_descoberto[jogador.y][jogador.x + 1] = mapa[jogador.y][jogador.x + 1]

    @staticmethod
    def descrever():
        print('\nA sala do mago é um refúgio de mistério e poder, situado em uma parte isolada do castelo.'
                '\nAs paredes são revestidas com tapeçarias enigmáticas que parecem mover-se levemente, como se impulsionadas por uma brisa invisível.'
                '\nLivros antigos e manuscritos empoeirados ocupam prateleiras de carvalho escuro, contendo conhecimentos arcanos e segredos perdidos.'
                '\nNo centro da sala, uma mesa de cristal brilha com runas esculpidas ao redor de sua borda, emanando uma luz suave e pulsante.'
                '\nUm círculo mágico intricadamente desenhado adorna o chão de pedra, cercado por velas acesas que projetam sombras dançantes nas paredes.'
                '\nFrascos de ingredientes exóticos e artefatos mágicos estão dispostos ordenadamente em bancadas de trabalho de mármore, cada um carregado com uma energia única e misteriosa.'
                '\nO ar está impregnado com o cheiro de ervas aromáticas e incenso, criando uma atmosfera de concentração e poder.'
                '\nUm caldeirão de bronze repousa sobre um tripé, emitindo ocasionalmente vapores coloridos que se dissipam no ar.'
                '\nA sala do mago é um local onde o conhecimento esotérico encontra-se com a prática mágica, um espaço onde o impossível se torna possível nas mãos habilidosas de seu misterioso ocupante.\n')

    def __str__(self):
        return 'Sala do Mago'


if __name__ == '__main__':
    print(Corredor.descrever())
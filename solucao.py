from collections import deque
from heapq import heapify, heappush, heappop
import numpy as np

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __lt__(self, other):
        return self.custo < other.custo

def sucessor(estado):
    """
    Recebe um estado (string) e retorna uma lista de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    def move_vazio(estado, direcao, flags):
        if direcao == 'direita' and flags['flag_direita'] != 1:
            shift = 1
        elif direcao == 'esquerda' and flags['flag_esquerda'] != 1:
            shift = -1
        elif direcao == 'acima' and flags['flag_acima'] != 1:
            shift = -3
        elif direcao == 'abaixo' and flags['flag_abaixo'] != 1:
            shift = 3
        else:
            return None
        string_list = list(estado)
        estado_alterado = string_list
        estado_alterado[estado.rfind('_')] = string_list[estado.rfind('_') + shift]
        estado_alterado[estado.rfind('_') + shift] = '_'
        estado = ''.join(estado_alterado)
        return estado

    posicao_vazio = estado.rfind('_')
    flags = {'flag_acima': 0, 'flag_abaixo': 0, 'flag_direita': 0, 'flag_esquerda': 0}
    sucessor = {}

    if posicao_vazio <= 2:
        flags['flag_acima'] = 1
    if posicao_vazio >= 6:
        flags['flag_abaixo'] = 1
    if(posicao_vazio == 2 or posicao_vazio == 5 or posicao_vazio == 8):
        flags['flag_direita'] = 1
    if(posicao_vazio == 0 or posicao_vazio == 3 or posicao_vazio == 6):
        flags['flag_esquerda'] = 1
    
    sucessor['acima'] = move_vazio(estado, 'acima', flags)
    sucessor['abaixo'] = move_vazio(estado, 'abaixo', flags)
    sucessor['direita'] = move_vazio(estado, 'direita', flags)
    sucessor['esquerda'] = move_vazio(estado, 'esquerda', flags)
    filtered = {k: v for k, v in sucessor.items() if v is not None}
    sucessor.clear()
    sucessor.update(filtered)
    lista_tuplas = list(sucessor.items())
    return lista_tuplas


def expande(nodo):
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um iterable de nodos.
    Cada nodo do iterable é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    sucessores_nodo = sucessor(nodo.estado)
    nodos = []
    for s in sucessores_nodo:
        nodos.append(Nodo(s[1], nodo, s[0], nodo.custo + 1))
    return nodos


def bfs(estado):
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha aabaixo pelo seu codigo
    GOAL = "12345678_"
    explorados = set()
    fronteira = deque([Nodo(estado, None, None, 0)])
    # i = 0
    while fronteira:
        # Remove do inicio da fila
        nodoAtual = fronteira.popleft()
        # i += 1
        # print(nodoAtual.estado)
        # print(i)

        # Encontrou solucao
        if nodoAtual.estado == GOAL:
            return pathTaken(nodoAtual)

        tupla_atual = (nodoAtual.acao, nodoAtual.estado)
        if tupla_atual not in explorados:
            explorados.add(tupla_atual)
            # Para cada acao possível cria um novo nodo e insere na fila
            for acao, estado in sucessor(nodoAtual.estado):
                fronteira.append(Nodo(estado, nodoAtual, acao, nodoAtual.custo + 1))

    # Nao alcancou estado final apos buscar todos estados possiveis
    # a partir da posicao inicial
    return None


def dfs(estado):
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha aabaixo pelo seu codigo
    GOAL = "12345678_"
    explorados = set()
    fronteira = deque([Nodo(estado, None, None, 0)])
    # i = 0
    while fronteira:
        nodoAtual = fronteira.pop()
        # i += 1
        # print(nodoAtual.estado)
        # print(i)
        # time.sleep(1)

        if nodoAtual.estado == GOAL:
            return pathTaken(nodoAtual)

        tupla_atual = (nodoAtual.acao, nodoAtual.estado)
        if tupla_atual not in explorados:
            explorados.add(tupla_atual)
            # Para cada acao possível cria um novo nodo e insere na fila
            for acao, estado in sucessor(nodoAtual.estado):
                if (acao, estado) not in explorados:
                    fronteira.append(Nodo(estado, nodoAtual, acao, nodoAtual.custo + 1))

    # Nao alcancou estado final apos buscar todos estados possiveis
    # a partir da posicao inicial
    return None


def astar_hamming(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha aabaixo pelo seu codigo
    def Hamming(estado):
        """
        Recebe um estado (string)
        Retorna um inteiro representando a distancia Hamming
        :param estado: str
        :return:
        Remove "_" do estado e compara com 12345678
        """
        estado = estado.replace("_","")
        numeroIdeal = 1
        erros = 0
        for numero in estado:
            if int(numero) != numeroIdeal :
                erros += 1
            numeroIdeal+=1
        return erros

    return astar_handler(estado, Hamming)


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    def Manhattan(estado):
        """
        Recebe um estado (string)
        calcula a distancia de cada numero a sua posical ideal
        Retorna soma todas as distancias Manhattan (int)
        :param estado: str
        :return:
        """
        # Posicao correta de cada elemento
        posicaoCorretaNumero = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1), '_': (2, 2)}
        # Transforma a string em um array (3,3)
        estado = np.asarray(list(estado)).reshape(3,3)

        # Compara o indice atual com indice de onde deveria estar
        distancia = 0
        for linha in range(3):
            for coluna in range(3):
                numeroAtual = estado[linha][coluna]
                # Cria uma tupla com a distancia manhatan (x,y) do numero atual
                # Soma x + y para obter a distancia final
                # Acumula a distancia de todas posicoes
                distancia += sum(tuple(map(lambda posicaoCorreta,posicaoAtual: abs(posicaoCorreta - posicaoAtual), posicaoCorretaNumero[numeroAtual],(linha, coluna))))
        return distancia

    return astar_handler(estado, Manhattan)
    

######################
# Funções Auxiliares #
######################

def astar_handler(estado, distanceCalc):
    """
    estado: str
    distanceCalc: funcao a ser utilizada para calcular a distancia de um estado ao
    estado final
    """
    explorados = set()
    fronteira = [ Nodo(estado, None, None, distanceCalc(estado)) ]
    heapify(fronteira)
    while fronteira:
        nodoAtual = heappop(fronteira)

        # Encontrou solucao
        if isFinalState(nodoAtual.estado): return pathTaken(nodoAtual)

        tupla_atual = (nodoAtual.acao, nodoAtual.estado)
        if tupla_atual not in explorados:
            explorados.add(tupla_atual)
            # Para cada acao possível cria um novo nodo e insere na fila
            for acao, estado in sucessor(nodoAtual.estado):
                heappush(fronteira, Nodo(estado, nodoAtual, acao, nodoAtual.custo + distanceCalc(estado)) )
    return None


def isFinalState(estado):
  return estado == "12345678_"


def pathTaken(nodo):
    """
    Recebe nodo
    Retorna uma lista de ações tomadas para se chegar ao nodo
    :param nodo: Nodo
    :return:
    """
    path = []
    # Vai de pai em pai gravando a acao tomada
    while nodo:
      path.append(nodo.acao)
      nodo = nodo.pai

    # Remove a acao None
    if path: 
      path.pop() 
    # Inverte a ordem das acoes
    return list(reversed(path))

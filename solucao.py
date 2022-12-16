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
        
    lista_estados = []
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
    estados = {}
    nodos = []
    for x in sucessores_nodo:
        mov, estado = x
        estados[mov] = estado

    for mov in estados:
        nodos.append(Nodo(estados[mov], nodo, mov, nodo.custo + 1))
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
    raise NotImplementedError


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
    raise NotImplementedError


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
    raise NotImplementedError


def astar_manhattan(estado):
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha aabaixo pelo seu codigo
    raise NotImplementedError

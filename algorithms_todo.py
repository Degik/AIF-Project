import numpy as np

from collections import deque
from queue import PriorityQueue
from utils import get_valid_moves
from typing import Tuple, List

def build_path(parent: dict, target: Tuple[int, int]) -> List[Tuple[int, int]]:
    #Costruisco il path vuoto
    path = []
    #Controllo che il target non sia nullo
    while target is not None:
        #Aggiungo il target al path (in coda alla lista)
        path.append(target)
        #Il target ovvero il precedente elemento del path per raggiungere target sarebbe il parent di target
        target = parent[target]
    #Alla fine del procedimento inverto e restituisco la lista
    path.reverse()
    return path

def bfs(game_map: np.ndarray, start: Tuple[int, int], target: Tuple[int, int]) -> List[Tuple[int, int]]:
    # Create a queue for BFS and mark the start node as visited
    #Dichiariamo la lista vuota queue con il metodo deque
    #Questo metodo e preferibile alla semplice queue = [] per motivi di efficienza
    #Le operazioni FIFO e LIFO sono altamente efficienti su questo tipo di lista
    queue = deque()
    #Dichiariamo la visited come l'insieme degli elementi già visitati
    #Stesso motivo di prima, molta efficienza in caso di operazioni add
    visited = set()
    #Tramite il metodo append inseriamo l'elemento start in coda alla queue
    queue.append(start)
    #Con il metodo add inseriamo start nell'insieme visited
    visited.add(start)

    # Create a dictionary to keep track of the parent node for each node in the path
    # Semplicemente teniamo traccia del percorso da effettuare
    parent = {start: None}

    while queue: #Ricordati che se la lista è vuota il while non viene eseguito
        # Dequeue a vertex from the queue
        #Nel nodo corrente eliminiamo l'elemento più a sinistra in lista queue e li ritorniamo in current, tutto con il metodo popleft
        #Ricordiamoci che questi sono gli elementi corrrenti, quindi spostadoci questa va liberata
        # Il metodo popleft in caso di lista vuota torna l'eccezione IndexError
        current = queue.popleft()

        # Check if the target node has been reached
        if current == target:
            print("Target found!")
            path = build_path(parent, target)
            return path

        # Visit all adjacent neighbors of the dequeued vertex
        #Controlliamo se il nodo (casella) vicino è valido come mossa
        for neighbor in get_valid_moves(game_map, current):
            #Controlliamo che il nodo non sia stato già visitato
            if neighbor not in visited:
                #Aggiungiamo il nodo in coda alla lista queue
                queue.append(neighbor)
                #Segnamo il nodo come già visitato
                visited.add(neighbor)
                #Segnamo sul percorso come parent di quel nodo la nostra current
                parent[neighbor] = current

    print("Target node not found!")
    return None

# ---------------------------------------------

def a_star(game_map: np.ndarray, start: Tuple[int, int], target: Tuple[int, int], h: callable) -> List[Tuple[int, int]]:
    # initialize open and close list
    open_list = PriorityQueue()
    close_list = []
    # additional dict which maintains the nodes in the open list for an easier access and check
    support_list = {}

    starting_state_g = ...
    starting_state_h = ...
    starting_state_f = ...

    open_list.put((starting_state_f, (start, starting_state_g)))
    support_list[start] = starting_state_g
    parent = {start: None}

    while not open_list.empty():
        # get the node with lowest f
        ... = open_list.get()
        # add the node to the close list
        close_list.append(current)

        if current == target:
            print("Target found!")
            path = build_path(parent, target)
            return path

        for neighbor in get_valid_moves(game_map, current):
            # check if neighbor in close list, if so continue
            ...

            # compute neighbor g, h and f values
            neighbor_g = ...
            neighbor_h = ...
            neighbor_f = ...
            parent[neighbor] = current
            neighbor_entry = (neighbor_f, (neighbor, neighbor_g))
            # if neighbor in open_list
            if neighbor in support_list.keys():
                # if neighbor_g is greater or equal to the one in the open list, continue
                ...

            # add neighbor to open list and update support_list
            ...
            support_list[...] = ...

    print("Target node not found!")
    return None

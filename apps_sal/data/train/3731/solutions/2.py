# ==========================================================================================================================================
# title         : squares, v2: faster with dictionnary instead of graph
# description   :
# author        : JR
# date          : 28.04.20
# version       :
# IDE           : PyCharm
# ==========================================================================================================================================
import math

# code standard graphs (dirty-duct-copy networkx behavior)


class nx(dict):
    @staticmethod
    def empty_graph(nodes):
        return nx(nodes)

    @staticmethod
    def squares_graph(n=23):
        square_candidates = [(x + 1)**2 for x in range(1, math.floor(math.sqrt(2 * n - 1)))]
        G = nx.empty_graph(list(range(1, n + 1)))

        for s in square_candidates:
            true_indexes = [x for x in range(1, 1 + math.floor((s - 1) / 2)) if s - x <= n]
            for k in true_indexes:
                G.add_edge(k, s - k)

        return G

    @staticmethod
    def Graph(G):
        # here we will implement the by-copy
        return nx(G.copy())

    def __init__(self, nodes, edges=None):
        if edges is None:
            if isinstance(nodes, dict):
                # by-copy => this one should not really be used for our problem, but it is simpler at the beginning to be able to concentrate
                # on the central matter
                dict.__init__(self, {n: e.copy() for n, e in list(nodes.items())})
            else:
                dict.__init__(self, {n: set() for n in nodes})
        else:
            dict.__init__(self, {nodes[i]: edges[i] for i in range(len(nodes))})

    def add_edge(self, x, y):
        self[x] |= {y}
        self[y] |= {x}

    def remove_edge(self, x, y):
        self[x] -= {y}
        self[y] -= {x}

    def remove_node(self, n):
        edges = self[n].copy()
        for e in edges:
            self.remove_edge(n, e)

        del self[n]

    def display(self):
        import matplotlib.pyplot as plt
        import networkx as true_nx
        plt.clf()
        true_nx.draw(true_nx.Graph(G), labels={x: x for x in G.nodes})
        plt.show()

    @property
    def nodes(self):
        return list(self.keys())

    @property
    def degree(self):
        return {(n, len(e)) for n, e in list(self.items())}


def square_sums_row(n):
    return dfs_travel(n)


def dfs_travel(G=23, visit_ordered=None, N=None, display=False, verbose=False):
    if isinstance(G, int):
        G = nx.squares_graph(G)

    if N is None:
        N = len(G.nodes)

    if visit_ordered is None:
        visit_ordered = []

    if len(visit_ordered) == N:
        if verbose:
            print('SUCCESS')
        return visit_ordered

    impossible_nodes = [n for n, d in G.degree if d == 0]
    if len(impossible_nodes) > 0:
        return False
    ending_nodes = [n for n, d in G.degree if d == 1]

    if len(ending_nodes) > 2:
        return False

    if len(visit_ordered) == 0:

        # We do the best guess to visit nodes by random... starting by most certain ones
        if len(ending_nodes) > 0:
            if verbose:
                print('Guess zero')
            return dfs_travel(G, [ending_nodes[-1]], N, verbose=verbose)  # if two, it will arrive at the second node !

        degrees = G.degree
        max_degree = max([y for x, y in degrees])
        for d in range(2, max_degree + 1):
            for n in [nd for nd, deg in degrees if deg == d]:
                sol = dfs_travel(G, [n], verbose=verbose)
                if sol != False:  # don't want the unsafe "if sol" with list
                    if verbose:
                        print('YESSS')
                    return sol

        if verbose:
            print('Exhausted guesses')
        return False

    elif len(ending_nodes) == 2 and not visit_ordered[-1] in ending_nodes:
        return False

    G2 = nx.Graph(G)  # copy the graph... will need to improve if >100 graphs are needed !

    last_idx = visit_ordered[-1]
    for current_idx in G2[last_idx]:  # .keys():
        if verbose:
            print((last_idx, current_idx))
        visit_ordered.append(current_idx)
        if verbose:
            print(visit_ordered)
        G3 = nx.Graph(G2)
        G3.remove_node(last_idx)
        sol = dfs_travel(G3, visit_ordered, N, verbose=verbose)

        if sol != False:
            return visit_ordered

        visit_ordered.pop()
    if verbose:
        print(visit_ordered)
        print((len(visit_ordered) - N))
    return False

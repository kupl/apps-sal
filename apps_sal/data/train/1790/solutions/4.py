class Graph():

    def __init__(self, vertices_num):
        self.v = vertices_num
        self.nodes = None

    def adjmat_2_graph(self, adjm):
        d = {}
        for indice, ligne in enumerate(adjm):
            print((indice, ligne))
            cle = 'A' + str(indice)
            laliste = []
            for indiceVoisin, nombre in enumerate(ligne):
                if nombre:
                    t = ('A' + str(indiceVoisin), nombre)
                    laliste.append(t)
            d[cle] = laliste
        return d

    def graph_2_mat(self, graph):
        m = [[0 for k in range(self.v)] for i in range(self.v)]
        for noeud in graph:
            indice = int(noeud[1:])
            for voisin in graph[noeud]:
                indiceVoisin = int(voisin[0][1:])
                distance = voisin[1]
                m[indice][indiceVoisin] = distance
        return m

    def graph_2_list(self, graph):
        m = []
        for noeud in graph:
            laliste = [noeud, graph[noeud]]
            m.append(laliste)
        m.sort()
        return m

    def list_2_graph(self, lst):
        d = {}
        for elt in lst:
            cle = elt[0]
            laliste = elt[1]
            d[cle] = laliste
        return d

    def mat_2_list(self, mat):
        d = self.adjmat_2_graph(mat)
        adj = self.graph_2_list(d)
        return adj

    def list_2_mat(self, lst):
        d = self.list_2_graph(lst)
        a = self.graph_2_mat(d)
        return a

    def find_all_paths(self, graph, start_vertex, end_vertex):
        if start_vertex == end_vertex:
            return [end_vertex]
        start_vertex = int(start_vertex[1:])
        end_vertex = int(end_vertex[1:])
        lesChemins = []
        m = self.graph_2_mat(graph)
        noeuds = list(range(self.v))

        pile = [[start_vertex]]
        while pile:
            chemin = pile.pop()
            dernier = chemin[-1]
            lesVoisins = [k for k in noeuds if m[dernier][k] > 0 and k not in chemin]
            for voisin in lesVoisins:
                if voisin == end_vertex:
                    bonChemin = chemin.copy()
                    bonChemin.append(voisin)
                    bonChemin = ['A' + str(k) for k in bonChemin]
                    lesChemins.append('-'.join(bonChemin))
                else:
                    leChemin = chemin.copy()
                    leChemin.append(voisin)
                    pile.append(leChemin)

        lesChemins.sort()
        lesChemins.sort(key=len)
        return lesChemins

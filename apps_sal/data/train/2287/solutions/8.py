class Graph:
    def __init__(self, n_vertices, edges, directed=True):
        self.n_vertices = n_vertices
        self.directed = directed
        self.edges = edges

    @property
    def adj(self):
        try:
            return self._adj
        except AttributeError:
            adj = [[] for _ in range(self.n_vertices)]
            if self.directed:
                for u,v in self.edges:
                    adj[u].append(v)
            else:
                for u,v in self.edges:
                    adj[u].append(v)
                    adj[v].append(u)
            self._adj = adj
            return adj


def solve(tree, vp):

    adj = tree.adj
    n = tree.n_vertices
    q = [v-1 for v,p in vp]
    ranges = [None]*n
    for v,p in vp:
        ranges[v-1] = (p,p)
    
    while q:
        nq = []
        for v in q:
            a,b = ranges[v]
            na,nb = a-1,b+1
            for u in adj[v]:
                if ranges[u] is None:
                    ranges[u] = na,nb
                    nq.append(u)
                else:
                    c,d = ranges[u]
                    if (c+na)%2 == 1:
                        return None
                    x,y = max(na,c),min(nb,d)
                    if x > y:
                        return None
                    ranges[u] = (x,y)
                    if (x,y) != (c,d):
                        nq.append(u)
        q = nq
    return [a for a,b in ranges]


def __starting_point():
    n = int(input())
    edges = [tuple(map(lambda x:int(x)-1,input().split())) for _ in range(n-1)]
    k = int(input())
    vp = [tuple(map(int,input().split())) for _ in range(k)]

    tree = Graph(n, edges, False)

    res = solve(tree, vp)
    if res is None:
        print('No')
    else:
        print('Yes')
        print(*res,sep='\n')
__starting_point()

import sys
import queue


class UF(object):
    def __init__(self, n):
        self.arr = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def root(self, x):
        if self.arr[x] != x:
            self.arr[x] = self.root(self.arr[x])
        return self.arr[x]

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)

        if root_x == root_y:
            return

        rank_x = self.rank[root_x]
        rank_y = self.rank[root_y]

        if rank_x >= rank_y:
            self.rank[root_x] += rank_y
            self.arr[root_y] = root_x
        else:
            self.rank[root_y] += rank_x
            self.arr[root_x] = root_y


n, m = sys.stdin.readline().split(" ")
n = int(n)
m = int(m)

# Do note that every other edge that isn't present in this list already connects nodes.


def load_graph(m, n):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = set()

    for _ in range(m):
        i, j = sys.stdin.readline().split(" ")
        i = int(i)
        j = int(j)
        graph[i].add(j)
        graph[j].add(i)
    return graph


def do(n, m):
    uf = UF(n)
    one_graph = load_graph(m, n)
    sorted_graph = sorted(one_graph, key=lambda x: len(one_graph[x]))
    if m < n - 1:
        return 0
    if m == n - 1 and n > 1:
        if len(one_graph[sorted_graph[-1]]) == n - 1:
            return 1
        else:
            return 0
    remaining = set(range(1, n + 1))

    for start in sorted_graph:
        if len(remaining) == 0:
            break
        if start not in remaining:
            continue

        Q = queue.Queue()
        Q.put(start)
        remaining.remove(start)
        while not Q.empty():
            u = Q.get()

            one_graph[u].intersection_update(remaining)
            # intersection are things you need to process but can't yet
            remaining.difference_update(one_graph[u])
            for elt in remaining:
                Q.put(elt)
                uf.union(u, elt)
            remaining = one_graph[u]
            if len(remaining) == 0:
                break
    return len(set(uf.arr)) - 2


res = do(n, m)
sys.stdout.write(str(res) + "\n")

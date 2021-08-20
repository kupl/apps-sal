from math import sqrt


class Graph:

    def __init__(self, connections):
        self.n = len(connections)
        self.connections = connections
        self.adjacency_matrix = [[0] * self.n for _ in range(self.n)]
        for (i, j) in enumerate(self.connections):
            for k in j:
                self.adjacency_matrix[i][k - 1] = 1

    def hamilton(self):
        for i in range(self.n):
            visited = [False] * self.n
            path = []

            def _hamilton(curr):
                path.append(curr)
                if len(path) == self.n:
                    return True
                visited[curr] = True
                for next in range(self.n):
                    if self.adjacency_matrix[curr][next] == 1 and (not visited[next]):
                        if _hamilton(next):
                            return True
                visited[curr] = False
                path.pop()
                return False
            if _hamilton(i):
                return [n + 1 for n in path]
        return False


def square_sums_row(n):
    connections = []
    temp = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if sqrt(i + j).is_integer():
                temp.append(j)
        connections.append([*temp])
        temp.clear()
    g = Graph(connections)
    return g.hamilton()

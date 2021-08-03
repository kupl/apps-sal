from queue import Queue
from collections import defaultdict


class PhilipTrains():
    def __init__(self, n, k, state):
        self.n = n
        self.k = k
        self.state = state
        self.graph = [[[0 for i in range(n + 1)] for j in range(n)] for k in range(3)]
        for i in range(len(state)):
            for j in range(len(state[i])):
                if 'A' <= state[i][j] <= 'Z':
                    for k in range(n):
                        nj = j - (2 * k)
                        if nj >= 0:
                            self.graph[i][nj][k] = -1
                        else:
                            break
        for i in range(len(state)):
            if state[i][0] == 's':
                self.r = i
                self.c = 0

    def check_reach(self):
        q = Queue()
        check = defaultdict(int)

        changes = [(1, 1, 1), (-1, 1, 1), (0, 1, 1)]

        q.put((self.r, self.c, 0))
        check[(self.r, self.c, 0)] = 1

        while not q.empty():
            pr, pc, pt = q.get()
            if self.graph[pr][pc][pt] == -1:
                continue
            if pc == self.n - 1:
                return 'YES'
            if self.graph[pr][pc + 1][pt] != -1:
                if check[(pr, pc + 1, pt + 1)] != 1:
                    q.put((pr, pc + 1, pt + 1))
                    check[(pr, pc + 1, pt + 1)] = 1
                for ch in [1, -1]:
                    if 0 <= pr + ch <= 2 and check[(pr + ch, pc + 1, pt + 1)] != 1 and self.graph[pr + ch][pc + 1][pt] != -1:
                        q.put((pr + ch, pc + 1, pt + 1))
                        check[(pr + ch, pc + 1, pt + 1)] = 1
        return 'NO'


t = int(input())

for i in range(t):
    n, k = list(map(int, input().strip(' ').split(' ')))
    arr = []
    for i in range(3):
        arr.append(input().strip(' '))
    graph = PhilipTrains(n, k, arr)
    print(graph.check_reach())

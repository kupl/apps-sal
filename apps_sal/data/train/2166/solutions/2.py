RESULT = ['Lose', 'Loop', 'Win']


class Player(object):
    """docstring for Player"""

    def __init__(self):
        super(Player, self).__init__()
        self.a = list(map(int, input().split()))[1:]
        self.f = [len(self.a)] * n
        self.f[0] = 0

    def prev(self, i):
        for x in self.a:
            if self.f[(i - x) % n] > 0:
                yield ((i - x) % n)

    def print_result(self):
        print(*[RESULT[min(x, 1)] for x in self.f[1:]])


n = int(input())
(a, b) = (Player(), Player())
q = [(a, b, 0), (b, a, 0)]
while q:
    (x, y, i) = q.pop()
    for j in y.prev(i):
        y.f[j] = -1
        for k in x.prev(j):
            x.f[k] -= 1
            if x.f[k] == 0:
                q.append((x, y, k))
a.print_result()
b.print_result()

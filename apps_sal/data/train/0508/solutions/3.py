import heapq


class BalancingTree:

    def __init__(self):
        self.p = []
        self.q = []

    def insert(self, x):
        heapq.heappush(self.p, x)

    def erase(self, x):
        heapq.heappush(self.q, x)

    def minimum(self):
        while self.q and self.p[0] == self.q[0]:
            heapq.heappop(self.p)
            heapq.heappop(self.q)
        return self.p[0] if self.p else -1


(n, q) = list(map(int, input().split()))
events = []
for _ in range(n):
    (s, t, x) = list(map(int, input().split()))
    events.append((s - x, 1, x))
    events.append((t - x, 0, x))
for _ in range(q):
    d = int(input())
    events.append((d, 2, 0))
events.sort()
bt = BalancingTree()
for (_, i, k) in events:
    if i == 1:
        bt.insert(k)
    elif i == 0:
        bt.erase(k)
    else:
        print(bt.minimum())

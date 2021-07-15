from random import uniform,seed
class Node:
    def __init__(self, val):
        self.nexts = []
        self.val = val
    def __getitem__(self, i):
        return self.nexts[i]
    def __setitem__(self, i, n):
        if i == len(self.nexts):
            self.nexts.append(n)
        else:
            self.nexts[i] = n
    def nval(self, i):
        return self.nexts[i].val if self.nexts[i] else 100000
class Skiplist:
    def __init__(self):
        self.prob = 0.25
        self.start = Node(-1)
    def level(self):
        return len(self.start.nexts)
    def grow(self, node):
        d = 0
        while d==0 or uniform(0, 1) < self.prob:
            node[d] = None
            if self.level()-1 < d:
                self.start[d] = node
            d += 1
        return d
    def findall(self, target: int) -> bool:
        # Invariance: cur.val < target <= rval
        cur = self.start
        for i in range(self.level()-1, -1, -1):
            while not cur.val<=target<=cur.nval(i):
                cur = cur[i]
            yield i, cur
    def search(self, target: int) -> bool:
        return any(p.nval(i)==target for i,p in self.findall(target))
    def add(self, num: int) -> None:
        preds = list(self.findall(num))
        cur = Node(num)
        d = self.grow(cur)
        for i, prev in reversed(preds[-d:]):
            cur[i] = prev[i]
            prev[i] = cur
    def erase(self, num: int) -> bool:
        preds = [p for i,p in self.findall(num)][::-1]
        if not preds or preds[0].nval(0) != num:
            return False
        rem = preds[0][0]
        for i, p in enumerate(preds):
            if p[i] is rem:
                p[i] = p[i][i]
        while self.start and self.start[self.level()-1] is None:
            self.start.nexts.pop()
        return True
            
    def debug(self):
        print(\"Depth = \", self.level())
        for i in range(self.level()):
            cur = self.start[i]
            level = []
            while cur:
                level.append(cur.val)
                cur = cur[i]
            print(\"Level\", i, level)

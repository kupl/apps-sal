from collections import defaultdict


class UF:

    def __init__(self):
        self.p = {}
        self.r = defaultdict(lambda: 1)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.r[x] > self.r[y]:
            self.p[y] = x
        elif self.r[x] < self.r[y]:
            self.p[x] = y
        else:
            self.p[x] = y
            self.r[y] += 1

    def find(self, x):
        if self.p.get(x, x) != x:
            self.p[x] = self.find(self.p.get(x, x))
        return self.p.get(x, x)


class Solution:

    def numComponents(self, head: ListNode, G: List[int]) -> int:
        uf = UF()
        gSet = set(G)
        prev = head.val
        head = head.next
        while head != None:
            curr = head.val
            if curr in gSet and prev in gSet:
                uf.union(curr, prev)
            head = head.next
            prev = curr
        resSet = set()
        for i in G:
            resSet.add(uf.find(i))
        return len(resSet)

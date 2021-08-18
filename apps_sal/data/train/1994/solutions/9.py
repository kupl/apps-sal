class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.r[x] < self.r[y]:
            self.p[x] = y
            self.r[y] += self.r[x]
        else:
            self.p[y] = x
            self.r[x] += self.r[y]


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        dsu = DSU(max(G) + 1)

        slow, fast = head, head.next
        while slow and fast:
            if slow.val in G and fast.val in G:
                dsu.union(slow.val, fast.val)
            slow, fast = slow.next, fast.next

        return len({dsu.find(x) for x in G})

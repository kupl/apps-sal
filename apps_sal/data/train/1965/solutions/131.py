class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0
        self.size = 1


class DisjointSet:
    def __init__(self, n):
        self.sets = {x: Node(x) for x in range(1, n + 1)}
        self.disjointSet = {x: self.sets[x] for x in range(1, n + 1)}

    def findSet(self, x):
        y = x
        while y.parent != y:
            y = y.parent
        z = x
        while z != y:
            tmp = z.parent
            z.parent = y
            z = tmp
        return y

    def link(self, x_val, y_val):
        x = self.sets[x_val]
        y = self.sets[y_val]
        if x.rank > y.rank:
            y.parent = x
            if y_val in self.disjointSet and y_val != x_val:
                del self.disjointSet[y_val]
                x.size += y.size
        elif x.rank < y.rank:
            x.parent = y
            if x_val in self.disjointSet and y_val != x_val:
                del self.disjointSet[x_val]
                y.size += x.size
        else:
            x.parent = y
            y.rank += 1
            if x_val in self.disjointSet and y_val != x_val:
                del self.disjointSet[x_val]
                y.size += x.size

    def union(self, x, y):
        self.link(self.findSet(self.sets[x]).val, self.findSet(self.sets[y]).val)


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DisjointSet(n)
        bob = DisjointSet(n)
        both = DisjointSet(n)
        type1 = 0
        type2 = 0
        type3 = 0
        for edge in edges:
            etype, a, b = edge
            if etype == 1:
                alice.union(a, b)
                type1 += 1
            elif etype == 2:
                bob.union(a, b)
                type2 += 1
            else:
                alice.union(a, b)
                bob.union(a, b)
                both.union(a, b)
                type3 += 1
        # print(alice.disjointSet)
        # print(bob.disjointSet)
        # print(both.disjointSet)
        # print(len(bob.disjointSet))

        if len(alice.disjointSet) != 1 or len(bob.disjointSet) != 1:
            return -1
        tmp = 0
        for key, val in list(both.disjointSet.items()):
            tmp += val.size - 1
        return type3 - tmp + type1 - (len(both.disjointSet) - 1) + type2 - (len(both.disjointSet) - 1)

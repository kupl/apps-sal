class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        L1 = []
        L2 = []
        L3 = []
        count1 = count2 = count3 = 0
        for edge in edges:
            if edge[0] == 1:
                L1.append(edge)
            elif edge[0] == 2:
                L2.append(edge)
            else:
                L3.append(edge)
        father = [0] * (n + 1)
        for i in range(1, n + 1):
            father[i] = i
        count3 = 0
        for edge in L3:
            (x, a, b) = edge
            count3 += self.union(a, b, father)
        father1 = father[:]
        for edge in L1:
            (x, a, b) = edge
            count1 += self.union(a, b, father1)
        father2 = father[:]
        for edge in L2:
            (x, a, b) = edge
            count2 += self.union(a, b, father2)
        for i in range(1, n + 1):
            if self.find(father1, i) != self.find(father1, 1):
                return -1
            if self.find(father2, i) != self.find(father2, 1):
                return -1
        return count1 + count2 + count3

    def union(self, a, b, father):
        fa = self.find(father, a)
        fb = self.find(father, b)
        if fa != fb:
            father[fa] = fb
            return 0
        else:
            return 1

    def find(self, father, a):
        if father[a] == a:
            return a
        father[a] = self.find(father, father[a])
        return father[a]

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.parent = None


class Component:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None


class Solution:

    def __init__(self):
        self.ds = {}

    def findSet(self, key):
        if key in self.ds:
            return self.ds[key]
        node = Node(key)
        component = Component()
        node.parent = component
        component.head = node
        component.tail = node
        component.length += 1
        self.ds[key] = component
        return component

    def unionSet(self, c1, c2):
        if c1.length < c2.length:
            (c1, c2) = (c2, c1)
        c1.tail.next = c2.head
        c1.tail = c2.tail
        tmp = c2.head
        while tmp:
            tmp.parent = c1
            self.ds[tmp.val] = c1
            tmp = tmp.__next__
        c1.length += c2.length

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            j = i + 1
            while j < n:
                edges.append((i, j, abs(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))))
                j += 1
        edges.sort(key=lambda x: x[2])
        cost = 0
        for edge in edges:
            c1 = self.findSet(edge[0])
            c2 = self.findSet(edge[1])
            if c1 != c2:
                self.unionSet(c1, c2)
                cost += edge[2]
        return cost

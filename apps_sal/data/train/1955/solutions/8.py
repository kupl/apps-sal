from typing import List
from collections import defaultdict


class DisjointSet:
    def __init__(self, n):
        self.makeSet(n)

    def makeSet(self, n):
        self.parent = [i for i in range(n)]

    def union(self, i, j):
        self.parent[self.find(i)] = self.find(j)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        sa = list(s)
        lens = len(s)
        ds = DisjointSet(lens)
        for pair in pairs:
            i = pair[0]
            j = pair[1]
            ip = ds.find(i)
            jp = ds.find(j)
            if ip != jp:
                ds.union(i, j)
        cm = defaultdict(lambda: [])
        for i in range(lens):
            ip = ds.find(i)
            cm[ip].append((i, sa[i]))
        for _, li in list(cm.items()):
            if li:
                lsv = sorted(li, key=lambda t: t[1])
                for i in range(len(li)):
                    sa[li[i][0]] = lsv[i][1]

        return ''.join(sa)


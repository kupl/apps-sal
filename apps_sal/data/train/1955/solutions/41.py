from collections import defaultdict
from typing import List


class DSU:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def make_set(self, val):
        self.parent[val] = val
        self.size[val] = 1

    def get_parent(self, val):
        if self.parent[val] == val:
            return val
        parent = self.get_parent(self.parent[val])
        self.parent[val] = parent
        return parent

    def union(self, val1, val2):
        parent1 = self.get_parent(val1)
        parent2 = self.get_parent(val2)

        if parent1 != parent2 and self.size[parent1] >= self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        elif parent1 != parent2 and self.size[parent1] < self.size[parent2]:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]

        return True


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        dsu = DSU()
        #   create set for every letter
        for i in range(len(s)):
            dsu.make_set(i)

        #   union connected letters
        for x, y in pairs:
            dsu.union(x, y)

        m = defaultdict(list)
        #   map dsu parent to list of valid letters
        for i in range(len(s)):
            parent = dsu.get_parent(i)
            m[parent].append(s[i])

        #   sort lists of strings
        for key, list_val in m.items():
            m[key] = sorted(list_val)

        res = []
        for j in range(len(s)):
            parent = dsu.get_parent(j)
            smallest_letter = m[parent].pop(0)
            res.append(smallest_letter)

        return ''.join(res)

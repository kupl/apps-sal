from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        array = [char for char in s]
        edges = defaultdict(list)
        for i, j in pairs:
            edges[i].append(j)
            edges[j].append(i)
        parents = {}
        components = defaultdict(list)
        for i in range(len(pairs)):
            for j in edges[i]:
                self.union(i, j, parents)
        for child, parent in list(parents.items()):
            components[self.find(parent, parents)].append(child)
        print(parents)
        print(components)
        for parent, children in list(components.items()):
            tmp = sorted([array[child] for child in children])
            print(tmp)
            components[parent] = sorted(children)
            for k in range(len(children)):
                array[components[parent][k]] = tmp[k]
        return ''.join(array)

    def union(self, i, j, parents):
        if not parents.get(i):
            parents[i] = i
        if not parents.get(j):
            parents[j] = j
        pi, pj = self.find(i, parents), self.find(j, parents)
        parents[pj] = pi
        parents[i] = pi

    def find(self, i, parents):
        while parents[i] != i:
            parents[i] = parents[parents[i]]
            i = parents[i]
        return parents[i]

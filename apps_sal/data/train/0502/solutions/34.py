class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        parents = {}

        def find(parents, i):
            c = i
            while parents[c] != c:
                c = parents[c]
            parents[i] = c
            return c

        def union(parents, i, j):
            parents[find(parents, i)] = find(parents, j)

        for u in range(len(graph)):
            if u not in parents:
                parents[u] = u
            for v in range(len(graph[u])):
                if v not in parents:
                    parents[v] = v
                if graph[u][v] == 1:
                    union(parents, u, v)

        malware_count = collections.defaultdict(int)
        for i in initial:
            malware_count[find(parents, i)] += 1
        comp_size = collections.defaultdict(int)
        for k in parents.keys():
            comp_size[find(parents, k)] += 1

        largest_comp = None
        largest_size = 0
        for i in initial:
            k = find(parents, i)
            v = malware_count[k]
            if v == 1:
                if comp_size[k] > largest_size:
                    largest_size = comp_size[k]
                    largest_comp = [i]
                elif comp_size[k] == largest_size:
                    largest_comp.append(i)
        if largest_comp:
            return min(largest_comp)
        return min(initial)

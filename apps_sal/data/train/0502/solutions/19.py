import heapq


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        nodes = set(initial)
        useless = set()
        best = 0
        initial.sort()
        index = initial[0]

        def dfs(start):
            count = 0
            stack = [start]
            visited = set()
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                if curr != start and curr in nodes:
                    useless.add(curr)
                    useless.add(start)
                visited.add(curr)
                count += 1
                for i in range(len(graph[curr])):
                    if graph[curr][i]:
                        stack.append(i)
            return count
        for i in initial:
            g = dfs(i)
            if i not in useless:
                if g > best:
                    best = g
                    index = i
        return index

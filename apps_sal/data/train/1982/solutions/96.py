from collections import defaultdict


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for pair in dislikes:
            graph[pair[0]].add(pair[1])
            graph[pair[1]].add(pair[0])
        colors = [0] * (N + 1)
        visited = set()

        def check(i):
            stack = [i]
            colors[i] = -1
            while stack:
                popped = stack.pop()
                color = colors[popped]
                visited.add(popped)
                for enemy in graph[popped]:
                    if colors[enemy] == color:
                        return False
                    colors[enemy] = -color
                    if enemy not in visited:
                        stack.append(enemy)
            return True
        for i in range(1, N + 1):
            if i in visited:
                continue
            if not check(i):
                return False
        return True

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adjacents = collections.defaultdict(list)
        for a, b in dislikes:
            adjacents[a].append(b)
            adjacents[b].append(a)
        colored = {}
        for i in range(N):
            if i not in colored:
                colored[i] = 0
                stack = [i]
                while stack:
                    node = stack.pop()
                    for neighbor in adjacents[node]:
                        if neighbor not in colored:
                            colored[neighbor] = 1 - colored[node]
                            stack.append(neighbor)
                        if colored[neighbor] == colored[node]:
                            return False
        return True

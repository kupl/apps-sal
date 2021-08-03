class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N < 2:
            return True

        # We can look at this as a graph problem, where we connect all the
        # numbers with all the numbers they dislike.
        #
        # If we have any cycles of odd length, then we return False
        #
        graph = {i: [] for i in range(1, N + 1)}
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        # part table to assign partition to each number
        part = [None for _ in range(N + 1)]

        def dfs(i, p):
            part[i] = p
            for j in graph[i]:
                if part[j] == p:
                    return False
                if part[j] is None and not dfs(j, p ^ 1):
                    return False
            return True

        for i in graph:
            if part[i] is None and not dfs(i, 1):
                return False
        return True

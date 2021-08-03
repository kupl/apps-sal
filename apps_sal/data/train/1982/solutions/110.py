class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # Solution taken from leetcode solution
        # Insight: I was thinking about the fact that we need to test whether
        # 1 or the other color works for every unvisited node. But, since the
        # graph is an undirected graph, there cannot be an unvisited node that
        # is connected to a visited node once the dfs ends for a connected
        # component

        # Process edges into adjacency list
        self.g = collections.defaultdict(list)
        for num1, num2 in dislikes:
            self.g[num1].append(num2)
            self.g[num2].append(num1)

        self.color = {}

        def dfs(node, c):
            if node in self.color:
                return self.color[node] == c
            else:
                self.color[node] = c
                for dest in self.g[node]:
                    # `1-c` to swap between 0 and 1
                    res = dfs(dest, 1 - c)
                    if not res:
                        return False
            return True

        for node in self.g:
            if node not in self.color:
                res = dfs(node, 0)
                if not res:
                    return False

        return True

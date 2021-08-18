class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

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

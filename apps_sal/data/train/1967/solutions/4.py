class Solution:
    def dfs(self, final, S, path, original):
        # print(path)
        if not S and len(path) > 2 and all([int(i) <= 2**31 - 1 for i in path]):
            final.append(path)
        for i in range(1, len(S) + 1):
            temp = int(S[:i])
            if i > 1 and S[:i][0] == '0':
                continue
            if int(S[:i]) >= 2**31 - 1:
                return
            if len(path) < 2 or (len(path) >= 2 and int(path[-1]) + int(path[-2]) == temp):
                self.dfs(final, S[i:], path + [S[:i]], original)

    def splitIntoFibonacci(self, S: str) -> List[int]:
        final = []
        path = []
        self.dfs(final, S, path, S)
        if final:
            return final[0]
        return []

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:

        res = []
        self.dfs(res, S, 0, [])
        return res[0] if res else []

    def dfs(self, res, S, index, path):
        if index == len(S) and len(path) >= 3:
            res.append(path[:])
            return

        for i in range(index + 1, len(S) + 1):
            if (i > index + 1 and S[index] == '0') or int(S[index:i]) > 2**31 - 1:
                return
            temp_num = int(S[index:i])
            if (len(path) >= 2 and temp_num == path[-1] + path[-2]) or len(path) < 2:
                path.append(temp_num)
                self.dfs(res, S, i, path)
                path.pop()

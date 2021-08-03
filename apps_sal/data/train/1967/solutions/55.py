class Solution:
    def splitIntoFibonacci(self, S: str):
        self.res = []
        self.dfs(S, [], 0)
        return self.res

    def dfs(self, S, temp, count):
        if not S and count >= 3:
            self.res = temp[:]
            return
        for step in range(1, len(S) + 1):
            val = S[:step]
            if str(int(val)) == val and 0 <= int(val) <= pow(2, 31) - 1:  # 防止前导 0 的出现
                if count < 2:
                    temp.append(int(val))
                    self.dfs(S[step:], temp, count + 1)
                    temp.pop()
                elif temp[count - 2] + temp[count - 1] == int(val):
                    temp.append(int(val))
                    self.dfs(S[step:], temp, count + 1)
                    temp.pop()

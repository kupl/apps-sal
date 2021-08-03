class Solution:

    def __init__(self):
        self.q = []

    def splitIntoFibonacci(self, s: str) -> List[int]:
        self.dfs(s, [], 0)
        return self.q

    def dfs(self, s, q, i):
        if i == len(s):
            if len(q) >= 3:
                self.q = q[::]
            return len(q) >= 3

        for j in range(i, min(len(s), i + 10)):
            v = int(s[i:j + 1])
            b1 = (v < 2 ** 31 - 1)
            b2 = v == 0 or (v and s[i] != '0')
            b3 = len(q) < 2 or (q[-1] + q[-2] == v)
            if b1 and b2 and b3 and self.dfs(s, q + [v], j + 1):
                return True
        return False

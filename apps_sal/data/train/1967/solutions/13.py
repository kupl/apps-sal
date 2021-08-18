class Solution:
    def dfs(self, grandpa, parent, S, start):
        if start >= len(S):
            return [], True
        for i in range(start + 1, len(S) + 1):
            sub = S[start: i]
            if len(sub) > 1 and sub[0] == '0':
                continue
            num = int(sub)
            if num > 2**31 - 1:
                continue
            if grandpa >= 0 and parent >= 0 and num != grandpa + parent:
                continue

            ans, found = self.dfs(parent, num, S, i)
            if grandpa < 0 and parent < 0 and len(ans) < 2:
                continue
            if found:
                return [num] + ans, True
        return [], False

    def splitIntoFibonacci(self, S: str) -> List[int]:
        return self.dfs(-1, -1, S, 0)[0]

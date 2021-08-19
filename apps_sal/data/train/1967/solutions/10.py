class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        (n, ans) = (len(S), [])

        def dfs(pos):
            if pos == n:
                return len(ans) >= 3
            num = 0
            for i in range(pos, n):
                if S[pos] == '0' and i == pos or S[pos] != '0':
                    num = num * 10 + ord(S[i]) - ord('0')
                    if num < 2 ** 31 - 1:
                        if len(ans) < 2 or ans[-1] + ans[-2] == num:
                            ans.append(num)
                            if dfs(i + 1):
                                return True
                            ans.pop()
            return False
        dfs(0)
        return ans

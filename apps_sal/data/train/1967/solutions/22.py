class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        ans = []

        def dfs(position):
            if position == n:
                return True if len(ans) > 2 else False
            num = 0
            for i in range(position, n):
                num = num * 10 + ord(S[i]) - ord('0')
                if num >= 2 ** 31:
                    break
                if len(ans) < 2 or ans[-1] + ans[-2] == num:
                    ans.append(num)
                    if dfs(i + 1):
                        return True
                    ans.pop()
                if i == position and S[i] == '0':
                    return False
            return False
        dfs(0)
        return ans

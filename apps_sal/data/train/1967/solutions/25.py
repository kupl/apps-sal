class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = []
        limit = 2 ** 31 - 1

        @lru_cache(None)
        def helper(n, prefix):
            nonlocal S, ans
            if n == len(S):
                ans = prefix
                return
            num = int(S[prefix[-2]:prefix[-1]]) + int(S[prefix[-1]:n])
            if S[n:].startswith(str(num)) and num <= limit:
                return helper(n + len(str(num)), prefix + (n,))
        for i in range(2, len(S) * 2 // 3 + 1):
            for j in range(1, i):
                helper(i, (0, j))
                if ans:
                    break
            if ans:
                break
        return [int(S[i:j]) for (i, j) in zip(ans, ans[1:] + (len(S),))] if ans else []

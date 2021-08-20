class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = []
        limit = 2 ** 31 - 1

        def helper(n, prefix):
            nonlocal S, ans
            if ans:
                return
            if n == len(S):
                ans = prefix
                return
            num = sum(prefix[-2:])
            if S[n:].startswith(str(num)) and num <= limit:
                return helper(n + len(str(num)), prefix + [num])
        for i in range(2, len(S) * 2 // 3 + 1):
            for j in range(1, i):
                helper(i, [int(S[:j]), int(S[j:i])])
        return ans

class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = []
        limit = 2 ** 31 - 1

        def helper(n, prefix):
            nonlocal S, ans
            if n == len(S):
                ans = prefix
                return
            num = sum(prefix[-2:])
            if S[n:].startswith(str(num)) and num <= limit:
                return helper(n + len(str(num)), prefix + [num])
        for i in range(2, min(20, len(S) * 2 // 3 + 1)):
            for j in range(max(1, i - 10), min(i, 10)):
                helper(i, [int(S[:j]), int(S[j:i])])
                if ans:
                    break
            if ans:
                break
        return ans

class Solution:

    def countLargestGroup(self, n: int) -> int:
        memo = {1: 1}
        for i in range(2, n + 1):
            if not i % 10:
                memo[i] = memo[i // 10]
            else:
                memo[i] = memo[i - 1] + 1
        D = defaultdict(int)
        for (k, v) in memo.items():
            D[v] += 1
        res = 0
        for k in D.keys():
            if D[k] == max(D.values()):
                res += 1
        return res

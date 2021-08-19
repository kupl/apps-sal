class Solution:

    def minIncrementForUnique(self, A: List[int]) -> int:
        cnt = [0 for i in range(80001)]
        (minv, ans, n) = (40001, 0, len(A))
        for i in A:
            cnt[i] += 1
            minv = min(minv, i)
        for i in range(minv, 80001):
            if not n:
                break
            if cnt[i] > 1:
                cnt[i + 1] += cnt[i] - 1
                ans += cnt[i] - 1
            if cnt[i] == 1:
                n -= 1
        return ans

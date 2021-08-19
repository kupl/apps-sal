class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)
        ans = 0
        waiting = 0
        for x in range(80000):
            if count[x] >= 2:
                # waiting.extend([x]*(count[x]-1))
                waiting += count[x] - 1
                ans -= x * (count[x] - 1)
            elif waiting > 0 and count[x] == 0:
                # ans += x - waiting.pop()
                waiting -= 1
                ans += x
        return ans

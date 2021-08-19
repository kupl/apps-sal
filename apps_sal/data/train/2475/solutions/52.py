class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        ans = 0
        for i in zip(*A):
            if list(i) != sorted(i):
                ans += 1
        return ans

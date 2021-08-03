class Solution:
    def minNumberOperations(self, t: List[int]) -> int:
        cnt = t[0]
        for i in range(1, len(t)):
            if t[i] > t[i - 1]:
                cnt += t[i] - t[i - 1]
        return cnt

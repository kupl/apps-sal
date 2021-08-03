class Solution:
    def minOperations(self, logs: List[str]) -> int:

        t = 0
        for i in logs:
            if i == '../':
                t = t - 1
            elif i == './':
                t = t
            else:
                t = t + 1
            if t < 0:
                t = 0
        return t

class Solution:

    def countLargestGroup(self, n: int) -> int:
        counts = {}
        m = 0
        for i in range(1, n + 1):
            t = i
            s = 0
            while t:
                s += t % 10
                t //= 10
            counts[s] = counts.setdefault(s, 0) + 1
            if m < counts[s]:
                m = counts[s]
        return sum((v == m for v in list(counts.values())))

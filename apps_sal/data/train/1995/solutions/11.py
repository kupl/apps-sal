class Solution:

    def carPooling(self, trips: List[List[int]], c: int) -> bool:
        (f, t) = (float('inf'), -1)
        b = collections.defaultdict(int)
        for (n, s, e) in trips:
            b[s] += n
            b[e] -= n
            f = min(f, s)
            t = max(t, e)
        for i in range(f, t + 1):
            b[i] += b[i - 1]
            if b[i] > c:
                return False
        return True

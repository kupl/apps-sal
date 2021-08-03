class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)

        for a, b, c in trips:
            d[b] += a
            d[c] -= a

        k = 0
        for t in sorted(d.keys()):
            k += d[t]
            if k > capacity:
                return False
        return True

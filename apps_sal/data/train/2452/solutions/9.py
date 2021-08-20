class Solution:

    def lastStoneWeight(self, st: List[int]) -> int:
        for i in range(len(st)):
            st[i] *= -1
        heapq.heapify(st)
        while len(st) > 1:
            (a, b) = (heapq.heappop(st), heapq.heappop(st))
            a *= -1
            b *= -1
            if b != a:
                heapq.heappush(st, b - a)
        return -1 * st[0] if len(st) == 1 else 0

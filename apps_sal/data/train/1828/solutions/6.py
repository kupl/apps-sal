class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        mp = collections.defaultdict(int)
        for b in barcodes:
            mp[b] += 1
        heap = []
        for (k, v) in list(mp.items()):
            heapq.heappush(heap, (-v, k))
        idx = 0
        n = len(barcodes)
        ans = [0] * n
        while heap:
            (f, v) = heapq.heappop(heap)
            f = -f
            while f > 0:
                ans[idx] = v
                idx += 2
                f -= 1
                if idx >= n:
                    idx = 1
        return ans

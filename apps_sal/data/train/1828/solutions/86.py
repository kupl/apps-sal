class Solution:
    def rearrangeBarcodes(self, S: List[int]) -> List[int]:
        if not S:
            return []

        d = collections.Counter(S)
        heap = []
        for key, value in list(d.items()):
            heapq.heappush(heap, [-value, key])

        res = []
        pre = heapq.heappop(heap)
        res.append(pre[1])

        while heap:
            cur = heapq.heappop(heap)
            res.append(cur[1])

            pre[0] += 1
            if pre[0] < 0:
                heapq.heappush(heap, pre)

            pre = cur

        if len(res) != len(S):
            return []
        else:
            return res

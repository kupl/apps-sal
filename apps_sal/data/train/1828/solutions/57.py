class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        queue = deque()
        heap = []
        d = {}
        res = []
        time = 0

        for code in barcodes:
            d[code] = d.get(code, 0) - 1

        for k, v in d.items():
            heapq.heappush(heap, (v, k))

        while heap or queue:
            if heap:
                count, code = heapq.heappop(heap)
                count += 1
                res.append(code)

                if count < 0:
                    queue.append([time + 1, (count, code)])

            if queue and queue[0][0] <= time:
                heapq.heappush(heap, queue.popleft()[1])

            time += 1

        return res

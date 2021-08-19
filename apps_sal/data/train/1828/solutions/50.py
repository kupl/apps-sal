class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) <= 1:
            return barcodes

        def helper(barcodes, k):
            freqCount = collections.defaultdict(int)
            for ele in barcodes:
                freqCount[ele] += 1
            result = []
            cooldown = collections.deque()
            heap = []
            for (key, value) in freqCount.items():
                heapq.heappush(heap, (-value, key))
            while len(heap) > 0:
                (count, element) = heapq.heappop(heap)
                count *= -1
                result.append(element)
                cooldown.append((count - 1, element))
                if len(cooldown) < k:
                    continue
                (cooldownCount, cooldownElement) = cooldown.popleft()
                if cooldownCount > 0:
                    heapq.heappush(heap, (-cooldownCount, cooldownElement))
            return result
        return helper(barcodes, 2)

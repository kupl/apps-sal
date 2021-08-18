class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        hash_map = dict()
        heap = list()
        result = [0] * len(barcodes)
        index = 0

        for bar_code in barcodes:
            hash_map[bar_code] = hash_map.get(bar_code, 0) + 1

        print(hash_map)
        for code, freq in hash_map.items():
            heap.append((-freq, code))

        heapq.heapify(heap)

        while heap:
            freq, code = heapq.heappop(heap)
            freq = abs(freq)
            while freq > 0:
                if index >= len(barcodes):
                    index = 1
                result[index] = code
                index += 2
                freq -= 1
        return result

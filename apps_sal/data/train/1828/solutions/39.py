class Solution:
    def update(self, freq, key, heap):
        if freq > 1:
            heappush(heap, (-1 * (freq - 1), key))
            
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq_map = defaultdict(int)
        heap = []
        res = []
        for n in barcodes:
            freq_map[n] += 1
        
        for key in list(freq_map.keys()):
            heappush(heap, (-1 * freq_map[key], key))
        
        while len(heap) > 0:
            freq_a, key_a = heappop(heap)
            res.append(key_a)
            
            if len(heap) == 0:
                break
            freq_b, key_b = heappop(heap)
            res.append(key_b)
            self.update(-1 * freq_a, key_a, heap)
            self.update(-1 * freq_b, key_b, heap)
        return res


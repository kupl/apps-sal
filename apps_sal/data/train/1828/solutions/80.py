class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        M = 0
        
        for k, v in cnt.items():
            if v>M:
                mark = k
                M = v
        
        barcodes.sort()
        pos = defaultdict(list)
        j = 0
        
        for i in range(len(barcodes)):
            if barcodes[i]!=mark:
                pos[j].append(barcodes[i])
                j = (j+1)%M
        
        ans = []
        
        for i in range(M):
            ans += [mark]+pos[i]
        
        return ans

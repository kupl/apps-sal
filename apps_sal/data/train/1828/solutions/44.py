class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freq = [0] * 10001
        maxFreqCode = 0
        for code in barcodes:
            freq[code] += 1
            if freq[code] > freq[maxFreqCode]:
                maxFreqCode = code
        (i, n) = (0, len(barcodes))
        ans = [0] * n
        for code in range(10001):
            if code == 0:
                code = maxFreqCode
            for _ in range(freq[code]):
                if i >= n:
                    i = 1
                ans[i] = code
                i += 2
            freq[code] = 0
        return ans

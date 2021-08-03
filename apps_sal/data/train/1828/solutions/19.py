class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        len_ = len(barcodes)
        freq = collections.Counter()
        maxFreqCode = 0
        for code in barcodes:
            freq[code] += 1
            if freq[code] > freq[maxFreqCode]:
                maxFreqCode = code

        i = 0
        ans = [0] * len_

        for _ in range(freq[maxFreqCode]):
            ans[i] = maxFreqCode
            i += 2
        freq[maxFreqCode] = 0

        for code in freq:
            for _ in range(freq[code]):
                if i >= len_:
                    i = 1
                ans[i] = code
                i += 2
            freq[code] = 0

        return ans

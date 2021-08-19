class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dicta = [0] * 10001
        max_word = 0
        for i in barcodes:
            dicta[i] += 1
            if dicta[i] > dicta[max_word]:
                max_word = i
        ans = [0 for i in range(len(barcodes))]
        idx = 0
        for i in range(dicta[max_word]):
            ans[idx] = max_word
            idx += 2
        dicta[max_word] = 0
        for j in range(10001):
            if dicta[j] > 0:
                for i in range(dicta[j]):
                    if idx >= len(barcodes):
                        idx = 1
                    ans[idx] = j
                    idx += 2
        return ans

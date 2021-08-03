class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        count = collections.Counter(barcodes)

        ans = [0] * len(barcodes)

        index = 0
        for key, freq in count.most_common():

            for _ in range(freq):
                if index >= len(barcodes):
                    index = 1
                ans[index] = key
                index += 2

        return ans

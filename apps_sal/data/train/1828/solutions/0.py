class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        if len(barcodes) < 2:
            return barcodes

        sorted_codes = sorted(barcodes)
        halfway = len(barcodes) // 2
        ans = [0] * (halfway * 2)
        ans[::2], ans[1::2] = sorted_codes[-halfway:], sorted_codes[:halfway]

        if len(barcodes) % 2 == 1:
            prev = None
            mid = sorted_codes[halfway]
            for i in range(len(ans) - 1):
                if ans[i] == mid:
                    i += 1
                elif ans[i] != prev:
                    ans.insert(i, mid)
                    break
                prev = ans[i]
        return ans

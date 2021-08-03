class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        keys = sorted(list(counter.keys()), key=lambda k: counter[k], reverse=True)
        numbers = []
        for key in keys:
            numbers.extend([key] * counter[key])
        ans = [0] * len(numbers)
        N = len(numbers)
        ans[::2] = numbers[:(N + 1) // 2]
        ans[1::2] = numbers[(N + 1) // 2:]
        return ans

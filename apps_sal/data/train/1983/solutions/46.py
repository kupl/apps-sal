class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.len = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
            self.len = 0
        elif num == 1:
            self.len += 1
            if len(self.nums) and isinstance(self.nums[-1], list):
                self.nums[-1][0] += 1
            else:
                self.nums.append([1])
        else:
            self.len += 1
            self.nums.append(num)

    def getProduct(self, k: int) -> int:
        if k > self.len:
            return 0
        (prod, idx) = (1, len(self.nums) - 1)
        while k > 0:
            if isinstance(self.nums[idx], list):
                k -= self.nums[idx][0]
            else:
                prod *= self.nums[idx]
                k -= 1
            idx -= 1
        return prod

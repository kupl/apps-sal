class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.max_zero_idx = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.max_zero_idx = max(self.max_zero_idx, len(self.nums))

        if not self.nums:
            self.nums.append(num)
        else:
            prev_prod = self.nums[-1] if self.nums[-1] != 0 else 1
            self.nums.append(num * prev_prod)

    def getProduct(self, k: int) -> int:
        left, right = len(self.nums) - 1 - k, len(self.nums) - 1
        if left == self.max_zero_idx:
            return self.nums[right]
        elif left > self.max_zero_idx:
            return self.nums[right] // self.nums[left]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

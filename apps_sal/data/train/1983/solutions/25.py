class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        self.nums.append(num)

    def getProduct(self, k: int) -> int:
        stop = len(self.nums) - k
        return(math.prod(self.nums[stop:]))


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

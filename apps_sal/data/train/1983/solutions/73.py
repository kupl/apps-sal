class ProductOfNumbers:

    def __init__(self):
        self.nums = []

    def add(self, num: int) -> None:
        i = len(self.nums)
        self.nums.append((num, i + 1))

    def getProduct(self, k: int) -> int:
        def update(i):
            cur, done = self.nums[i]
            if done < len(self.nums):
                update(done)
                cur *= self.nums[done][0]
                self.nums[i] = cur, len(self.nums)

        count = len(self.nums)
        i = count - k
        cur, done = self.nums[i]
        if done < count:
            update(i)
        return self.nums[i][0]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

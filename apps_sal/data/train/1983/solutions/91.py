class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.curr_prod = None
        self.product_array = []
        self.zero_idx = set()

    def add(self, num: int) -> None:
        self.nums.append(num)
        if self.curr_prod == None or self.curr_prod == 0:
            self.product_array.append(num)
        else:
            self.product_array.append(self.curr_prod * num)
        self.curr_prod = self.product_array[-1]
        if num == 0:
            self.zero_idx.add(len(self.nums) - 1)

    def getProduct(self, k: int) -> int:
        if k == 1:
            return self.nums[-1]
        n = len(self.nums)
        for idx in self.zero_idx:
            if idx > n - k - 1 and idx < n:
                return 0
        if self.product_array[n - k - 1] == 0 or k == n:
            return self.product_array[n - 1]
        else:
            return int(self.product_array[n - 1] / self.product_array[n - k - 1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

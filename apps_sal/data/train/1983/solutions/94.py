
class ProductOfNumbers:

    def __init__(self):
        self.total_list = []
        self.cumul_list = [1]

    def add(self, num: int) -> None:
        self.total_list.append(num)
        if num == 0:
            self.cumul_list = [1]
        else:
            self.cumul_list.append(self.cumul_list[len(self.cumul_list) - 1] * num)

    def getProduct(self, k: int) -> int:
        if k < len(self.cumul_list):
            return int(self.cumul_list[len(self.cumul_list) - 1] / self.cumul_list[len(self.cumul_list) - k - 1])
        else:
            return 0

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

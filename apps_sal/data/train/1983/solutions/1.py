class ProductOfNumbers:

    def __init__(self):
        self.preprod = [1]

    def add(self, num: int) -> None:
        if not num:
            self.preprod = [1]
        else:
            self.preprod.append(self.preprod[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.preprod):
            return 0
        return self.preprod[-1] // self.preprod[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# 20

#[2, 10, 40]

#

#
# 3 0  2 , 5 ,4

# 3, 0, 2 ,5 ,4, 0


# []


# [1]
# return 0
# 0  0  40  20  4 0 1

class ProductOfNumbers:

    def __init__(self):
        self.mylist = []

    def add(self, num: int) -> None:
        self.mylist.append(num)

    def getProduct(self, k: int) -> int:
        this_list = self.mylist[-k:]
        return math.prod(this_list)

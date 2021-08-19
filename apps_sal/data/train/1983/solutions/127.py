from sortedcontainers import SortedList


class ProductOfNumbers:

    def __init__(self):
        self.product = []
        self.zero_index = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zero_index.append(len(self.product))
        if len(self.product) == 0:
            self.product.append(num)
            return
        tail = self.product[len(self.product) - 1]
        if tail == 0:
            self.product.append(num)
        else:
            self.product.append(num * tail)

    def getProduct(self, k: int) -> int:
        to_look = len(self.product) - k - 1
        if to_look < 0:
            if not self.zero_index:
                return self.product[len(self.product) - 1]
            else:
                return 0
        sorted_list = SortedList(self.zero_index)
        to_be_inserted = sorted_list.bisect_left(to_look + 1)
        if to_be_inserted != 0 and to_be_inserted < len(self.zero_index):
            return 0
        elif to_be_inserted == 0:
            if self.zero_index:
                return 0
        if self.product[to_look] == 0:
            return self.product[len(self.product) - 1]
        return self.product[len(self.product) - 1] // self.product[to_look]

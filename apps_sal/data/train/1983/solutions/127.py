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

    # TODO: essentially need to get the closest 0 that's greater than len(self.product) - k - 1
    def getProduct(self, k: int) -> int:
        to_look = len(self.product) - k - 1

        if to_look < 0:
            if not self.zero_index:
                return self.product[len(self.product)-1]
            else:
                return 0
        
        # now check whether or not there is a zero after the to_look index
        sorted_list = SortedList(self.zero_index)
        to_be_inserted = sorted_list.bisect_left(to_look+1)
        # TODO: i think this logic here is kind of wrong
        if to_be_inserted != 0 and to_be_inserted < len(self.zero_index):
            return 0
        elif to_be_inserted == 0:
            if self.zero_index:
                return 0

        # check whether or not to_look_index is 0 or not
        if self.product[to_look] == 0:
            return self.product[len(self.product)-1]

        return self.product[len(self.product)-1] // self.product[to_look]




# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)


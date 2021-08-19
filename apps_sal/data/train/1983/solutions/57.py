class Node:
    def __init__(self, previous, value):
        self.previous = previous
        self.value = value


class ProductOfNumbers:

    def __init__(self):
        self.endNode = None
        self.lastZero = None
        self.size = 0
        self.products = None

    def add(self, num: int) -> int:
        if (num == 0):
            self.lastZero = self.size

        self.size += 1

        self.products = dict()

        self.endNode = Node(self.endNode, num)

    def getProduct(self, k: int) -> None:
        if self.lastZero and self.size - k < self.lastZero:
            return 0

        if k in self.products:
            return self.products[k]

        product = 1
        currentNode = self.endNode
        for i in range(0, k):
            product *= currentNode.value
            currentNode = currentNode.previous

        self.products[k] = product
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

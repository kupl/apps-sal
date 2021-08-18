import queue as Q


class Node:
    def __init__(self):
        self.prev = None
        self.value = None


class ProductOfNumbers:

    def __init__(self):
        self.tail = None
        self.maxVal = float('-inf')

    def add(self, num: int) -> None:

        if num > self.maxVal:
            self.maxVal = num

        if self.tail == None:
            self.tail = Node()
            self.tail.value = num
            return

        temp = self.tail
        newNode = Node()
        newNode.value = num
        newNode.prev = temp
        self.tail = newNode

    def getProduct(self, k: int) -> int:
        if self.maxVal == 1:
            return 1

        result = 1
        count = 0
        temp = self.tail
        while count < k:
            result *= temp.value
            if result == 0:
                return 0
            temp = temp.prev
            count += 1
        return result

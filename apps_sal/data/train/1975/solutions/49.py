import numpy


class CustomStack:

    def __init__(self, maxSize: int):
        self.sz = maxSize
        self.vals = []

    def push(self, x: int) -> None:
        if len(self.vals) < self.sz:
            self.vals.append(x)

    def pop(self) -> int:
        if len(self.vals) > 0:
            return self.vals.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        tmp = numpy.array(self.vals)
        tmp[:k] += val
        self.vals = list(tmp)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

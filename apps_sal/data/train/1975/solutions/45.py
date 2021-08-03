class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.array = []
        self.size = 0

    def push(self, x: int) -> None:
        if self.size == self.max:
            pass
        else:
            self.array.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        temp = self.array.pop()
        return temp

    def increment(self, k: int, val: int) -> None:
        self.array[0:k] = list([x + val for x in self.array[0:k]])


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

class CustomStack:

    def __init__(self, maxSize: int):
        self.origin_list = [0] * maxSize
        self.index = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.index < self.maxSize:
            self.origin_list[self.index] = x
            self.index += 1

    def pop(self) -> int:
        if self.index == 0:
            return -1
        else:
            self.index -= 1
            return self.origin_list[self.index]

    def increment(self, k: int, val: int) -> None:
        num = min(k, self.index)
        for i in range(num):
            self.origin_list[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

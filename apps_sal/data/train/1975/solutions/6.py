class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.capacity = maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size < self.capacity:
            self.arr.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size > 0:
            ele = self.arr.pop()
            self.size -= 1
            return ele
        return -1

    def increment(self, k: int, val: int) -> None:
        k = min(k, self.size)
        for i in range(k):
            self.arr[i] += val

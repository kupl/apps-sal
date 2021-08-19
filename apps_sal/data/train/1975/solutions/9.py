class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.arr = []
        self.currsize = 0

    def push(self, x: int) -> None:
        if self.currsize == self.size:
            return
        self.arr.append(x)
        self.currsize += 1

    def pop(self) -> int:
        if len(self.arr) == 0:
            return -1
        self.currsize -= 1
        return self.arr.pop()

    def increment(self, k: int, val: int) -> None:
        minsize = min(k, len(self.arr))
        for i in range(minsize):
            self.arr[i] += val

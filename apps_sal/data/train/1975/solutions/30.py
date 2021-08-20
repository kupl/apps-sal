class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.curr_size = 0

    def push(self, x: int) -> None:
        if self.maxSize > self.curr_size:
            self.stack.append(x)
            self.curr_size += 1

    def pop(self) -> int:
        if len(self.stack):
            x = self.stack.pop()
            self.curr_size -= 1
            return x
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            for i in range(len(self.stack)):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val

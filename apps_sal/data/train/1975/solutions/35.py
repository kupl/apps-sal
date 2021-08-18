class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i <= len(self.stack) - 1:
                self.stack[i] += val

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        return (self.stack.pop() if self.stack else -1)

    def increment(self, k: int, val: int) -> None:
        for n in range(0, k):
            if n > len(self.stack) - 1:
                break
            else:
                self.stack[n] += val

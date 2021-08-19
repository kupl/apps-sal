class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        return -1 if not self.stack else self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        self.stack = [x + val if i < k else x for (i, x) in enumerate(self.stack)]

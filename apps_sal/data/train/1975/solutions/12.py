class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            num = self.stack[-1]
            self.stack.pop()
            return(num)
        else:
            return(-1)

    def increment(self, k: int, val: int) -> None:
        if k > len(self.stack):
            k = len(self.stack)
        for i in range(k):
            self.stack[i] = self.stack[i] + val

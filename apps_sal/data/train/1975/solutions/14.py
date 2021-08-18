class CustomStack:

    def __init__(self, maxSize: int):
        self.n = maxSize
        self.s = []

    def push(self, x: int) -> None:
        if len(self.s) < self.n:
            self.s.append(x)

    def pop(self) -> int:
        if len(self.s) == 0:
            return -1
        return self.s.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(0, k):
            if i >= len(self.s):
                break
            self.s[i] += val

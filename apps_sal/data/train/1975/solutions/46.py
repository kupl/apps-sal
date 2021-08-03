class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) >= 1:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        import numpy as np
        if k >= len(self.stack):
            self.stack = (np.array(self.stack) + np.array([val] * len(self.stack))).tolist()

        if k < len(self.stack):
            t = [val] * k
            t.extend([0] * (len(self.stack) - k))
            self.stack = (np.array(self.stack) + np.array(t)).tolist()

# ed and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.add = []
        self.limit = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.limit:
            self.stack.append(x)
            self.add.append(0)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        result = self.stack.pop()
        left = self.add.pop()
        if len(self.add) > 0:
            self.add[-1] += left
        return result + left

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) > 0:
            if k > len(self.stack):
                self.add[-1] += val
                return
            self.add[k - 1] += val

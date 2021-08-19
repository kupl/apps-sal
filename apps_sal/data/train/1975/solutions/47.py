class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.stack = []
        self.inc_stack = []
        self.index = 0

    def push(self, x: int) -> None:
        self.index += 1
        if len(self.stack) != self.max:
            self.stack.append((self.index, x))

    def pop(self) -> int:
        self.index += 1
        if not self.stack:
            return -1
        height = len(self.stack)
        index_x, x = self.stack.pop()
        for i in range(len(self.inc_stack) - 1, -1, -1):
            index, val, h = self.inc_stack[i]
            if index < index_x:
                break
            if h >= height:
                x += val
        return x

    def increment(self, k: int, val: int) -> None:
        self.index += 1
        self.inc_stack.append((self.index, val, min(k, len(self.stack))))


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

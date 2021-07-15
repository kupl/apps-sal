class CustomStack:

    def __init__(self, maxSize: int):
        self.items = []
        self.max = maxSize

    def push(self, x: int) -> None:
        if len(self.items) < self.max:
            self.items.append(x)

    def pop(self) -> int:
        return self.items.pop() if len(self.items) != 0 else -1

    def increment(self, k: int, val: int) -> None:
        k = k if k < len(self.items) else len(self.items)
        for i in range(k):
            self.items[i] = self.items[i] + val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


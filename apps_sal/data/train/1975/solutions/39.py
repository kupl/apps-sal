class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stk = []

    def push(self, x: int) -> None:
        if len(self.stk) == self.size:
            return
        else:
            self.stk.append(x)

    def pop(self) -> int:
        if len(self.stk) == 0:
            return -1
        else:
            return self.stk.pop()

    def increment(self, k: int, val: int) -> None:
        if len(self.stk) <= k:
            for i in range(len(self.stk)):
                self.stk[i] += val
        else:
            for i in range(0, k):
                self.stk[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

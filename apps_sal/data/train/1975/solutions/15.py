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
        # if k>len(self.stack):
        #     self.stack = list(map(lambda x:x+val, self.stack))
        # else:
        #     temp = []
        #     m = len(self.stack)-k
        #     while m:
        #         temp.append(self.stack.pop())
        #         m-=1
        #     self.stack = [x+val for x in self.stack]
        #     while temp:
        #         self.stack.append(temp.pop())


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

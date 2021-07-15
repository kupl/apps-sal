class CustomStack:

    def __init__(self, maxSize: int):
        self.customstack = []
        self.maxsize = maxSize
        
    def push(self, x: int) -> None:
        if len(self.customstack) != self.maxsize:
            self.customstack.append(x)

    def pop(self) -> int:
        if self.customstack != []:
            ele = self.customstack[-1]
            del self.customstack[-1]
            return ele
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        print(self.customstack)
        print(\"k\", k)
        print(\"value\", val)
        for i in range(min(k, len(self.customstack))):
            self.customstack[i] = self.customstack[i] + val
        print(self.customstack)
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = {}
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        print(\"push\",x)
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            # self.printStack()

    def pop(self) -> int:
        print(\"pop\")
        l = len(self.stack)
        if l:
            top = self.getTop()
            if l in self.inc:

                if l-1 in self.inc:
                    self.inc[l-1] += self.inc[l]
                else:
                    self.inc[l-1] = self.inc[l]
                del self.inc[l]
            
            self.stack.pop()
            # self.printStack()
            return top
        # self.printStack()
        return -1

    def increment(self, k: int, val: int) -> None:
        print(\"inc\",k,\"\",val)
        if k > len(self.stack):
            k = len(self.stack)
        if k in self.inc:        
                self.inc[k] += val
                # self.printStack()
        else:
            self.inc[k] = val
            # self.printStack()
        
    
    def getTop(self):
        
        if len(self.stack) == 0:
            # self.printStack()
            return -1
        else:
            l = len(self.stack)
            top = self.stack[-1]
            if l in self.inc:
                top+= self.inc[l]
            # self.printStack()
            return top
        
    def printStack(self):
        print(self.stack)
        print(self.inc)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

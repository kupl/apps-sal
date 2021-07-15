class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            
        

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop(-1)
            
            

    def increment(self, k: int, val: int) -> None:
        i = 0
        if k <= len(self.stack):
            while i < k:
                self.stack[i] += val
                i += 1
        else:
            while i < len(self.stack):
                self.stack[i] += val
                i += 1            
            
        
            
        
            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


class CustomStack:
    \"\"\"
    xxxxxxxxx i
         2
      2     5
    999777555      
      
    \"\"\"
    
    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        # print(self.inc)
        # print(self.stack)
        length = len(self.stack)
        if length > 0:
            increment = self.inc[-1]
            if length > 1:
                self.inc[length-2] += increment
            
            self.inc.pop()

            return self.stack.pop() + increment
        
        return -1

    def increment(self, k: int, val: int) -> None:
        if k <= len(self.inc):
            self.inc[k-1] += val
        elif len(self.inc) > 0:
            self.inc[-1] += val
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.size=maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
            # print(s)


    def pop(self) -> int:
        if len(self.stack)==0:
               return -1
        else:
            item=self.stack.pop()
            return item

    def increment(self, k: int, val: int) -> None:
        l=len(self.stack)
        if l < k:
            for i in range(len(self.stack)):
                # print(self.stack)
                self.stack[i]=self.stack[i]+val
        else:
            for i in range(0,k):
                self.stack[i]=self.stack[i]+val
                
            


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


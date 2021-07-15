class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=deque()
        self.limit=maxSize
        self.count=0

    def push(self, x: int) -> None:
        if self.count<self.limit:
            self.count+=1
            self.stack.append(x)
        

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            self.count-=1
            return self.stack.pop()
        

    def increment(self, k: int, val: int) -> None:
        tstack=[]
        while(self.stack and k>0):
            tstack.append(self.stack.popleft()+val)
            k-=1
        while(tstack):
            self.stack.appendleft(tstack.pop())
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


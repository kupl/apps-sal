class CustomStack:

    def __init__(self, maxSize: int):
        self.arr=[]
        self.size=maxSize
    def push(self, x: int) -> None:
        if(len(self.arr)==self.size):
            pass
        else:
            self.arr.append(x)
    def pop(self) -> int:
        try:
            return self.arr.pop()
        except:
            return -1
    def increment(self, k: int, val: int) -> None:
        ctr=0
        for i in self.arr:
            self.arr[ctr]+=val
            ctr+=1
            if(ctr==k):
                break


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


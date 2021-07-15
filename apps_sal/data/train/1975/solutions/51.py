class CustomStack:

    def __init__(self, maxSize: int):
       
        #if not len(self.lst) == maxSize:
        self.m = maxSize
        self.lst = []

    def push(self, x: int) -> None:
        if len(self.lst) < self.m:
            self.lst.append(x)

    def pop(self) -> int:
        if len(self.lst) == 0:
            return -1
        ret = self.lst[-1]
        self.lst = self.lst[0:-1]
        return ret

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < len(self.lst) and i < k:
            self.lst[i] += val
            i+=1
    


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


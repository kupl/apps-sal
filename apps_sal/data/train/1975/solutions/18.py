class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.storage = []
        

    def push(self, x: int) -> None:
        if len(self.storage) == self.max:
            return None
        self.storage.append(x)
        

    def pop(self) -> int:
        if len(self.storage) == 0:
            return -1
        return self.storage.pop()
        

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i == len(self.storage):
                return None
            self.storage[i] += val
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


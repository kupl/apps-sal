class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.capacity = capacity
        self.toPush = None

    def push(self, val: int) -> None:
        if not self.stacks:
            self.stacks.append([val])
            self.toPush = 0

        else:
            self.stacks[self.toPush].append(val)
                
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
            
        while len(self.stacks[self.toPush]) == self.capacity:
            self.toPush += 1

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop() 
            self.toPush = min(self.toPush, len(self.stacks)-1)
        
        if not self.stacks:
            return -1
        
        return self.stacks[-1].pop()

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and self.stacks[index]:
            self.toPush = min(self.toPush, index)
            return self.stacks[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


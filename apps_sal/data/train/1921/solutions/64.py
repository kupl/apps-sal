class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.leftFreeIndex = 0
        self.rightOccupiedIndex = 0
    
    def seek_head(self):
        while self.leftFreeIndex < len(self.stacks) and len(self.stacks[self.leftFreeIndex]) == self.capacity:
            self.leftFreeIndex += 1
    
    def seek_tail(self):
        while self.rightOccupiedIndex > 0 and len(self.stacks[self.rightOccupiedIndex]) == 0:
            self.rightOccupiedIndex -= 1
        
    def push(self, val: int) -> None:
        if not self.stacks:
            self.stacks.append([])
            
        self.stacks[self.leftFreeIndex].append(val)
        self.rightOccupiedIndex = max(self.leftFreeIndex, self.rightOccupiedIndex)
        
        if len(self.stacks[self.leftFreeIndex]) == self.capacity:
            self.seek_head()
            if len(self.stacks) == self.leftFreeIndex:
                self.stacks.append([])
        
    def pop(self) -> int:
        #print('pop: ', self.stacks)
        if not self.stacks:
            #print('stacks is empty, no more stacks')
            return -1
        
        if self.stacks[self.rightOccupiedIndex]:
            val = self.stacks[self.rightOccupiedIndex].pop(-1)
            self.seek_tail()
            return val
        
        return -1

    def popAtStack(self, index: int) -> int:
        #print('popAtStack: ', index, ' with current stacks: ', self.stacks)
        if index > len(self.stacks)-1:
            #print('stack at index doesnt exists')
            return -1
        
        if index == self.rightOccupiedIndex and index < self.leftFreeIndex:
            val = self.stacks[index].pop(-1)
            self.leftFreeIndex = index
            self.seek_tail()
            return val
        
        if index < self.leftFreeIndex:
            val = self.stacks[index].pop(-1)
            self.leftFreeIndex = index
            return val
        
        if index == self.rightOccupiedIndex:
            val = self.stacks[index].pop(-1)
            self.seek_tail()
            return val
        
        if self.stacks[index]:
            return self.stacks[index].pop(-1)
        
        return -1
# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []
        
    def push(self, val: int) -> None:
        if not self.available:
            self.stacks.append([])
            self.available.append(len(self.stacks) - 1)
        slot = self.available[0]
        self.stacks[slot].append(val)
        if len(self.stacks[slot]) == self.capacity:
            heapq.heappop(self.available)
            self.remove_empty_stacks()
    
    def remove_empty_stacks(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        while self.available and self.available[0] >= len(self.stacks):
            heapq.heappop(self.available)
        
    def pop(self) -> int:
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        result = self.stacks[index].pop()
        if len(self.stacks[index]) == self.capacity - 1:
            heapq.heappush(self.available, index)
        self.remove_empty_stacks()
        return result


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


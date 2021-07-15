class DinnerPlates:
    #Use heap to store index of available stack
    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks = []
        self.heap = []

    def push(self, val: int) -> None:
        if not self.heap:
            self.stacks.append([val])
            if len(self.stacks[-1]) < self.cap:
                heapq.heappush(self.heap, len(self.stacks)-1)
        else:
            i = heapq.heappop(self.heap)
            while self.heap and i < len(self.stacks) and len(self.stacks[i]) >= self.cap: 
                i = heapq.heappop(self.heap)
            if i >= len(self.stacks):
                self.stacks.append([val])
            
            else:
                self.stacks[i].append(val)
            if len(self.stacks[i]) < self.cap:
                heapq.heappush(self.heap, i)
            

    def pop(self) -> int:
        return self.popAtStack(len(self.stacks)-1)

    def popAtStack(self, index: int) -> int:
        if self.stacks == []: return -1
        if index < len(self.stacks) and self.stacks[index] == []: return -1
        
        if index < len(self.stacks) and self.stacks[index] != []: 
            item = self.stacks[index].pop()
            if self.stacks[index] == [] and index == len(self.stacks) - 1:
                while self.stacks and self.stacks[-1] == []:
                    self.stacks.pop()
            else:
                heapq.heappush(self.heap, index)
                
            return item
        return -1

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


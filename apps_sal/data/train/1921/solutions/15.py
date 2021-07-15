import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.leftmost = []
        self.K = capacity

    def push(self, val: int) -> None:
        if len(self.leftmost) == 0:
            if self.K != 1:
                self.leftmost.append(len(self.stacks))
            self.stacks.append([val])
        else:
            ind = self.leftmost[0]
            if ind >= len(self.stacks):
                self.stacks.append([])
            self.stacks[ind].append(val)
            if len(self.stacks[ind]) == self.K:
                heapq.heappop(self.leftmost)
            
    def pop(self) -> int:
        if len(self.stacks) == 0:
            return -1
            
        while len(self.stacks[-1]) == 0:
            self.stacks.pop()
            if len(self.stacks) == 0:
                return -1
            
        if len(self.stacks[-1]) == self.K:
            heapq.heappush(self.leftmost,len(self.stacks)-1)
            
        return self.stacks[-1].pop()

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1
        else:
            stack = self.stacks[index]
            if len(stack) == 0:
                return -1
            
            if len(stack) == self.K:
                heapq.heappush(self.leftmost,index)
            
            return stack.pop()
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


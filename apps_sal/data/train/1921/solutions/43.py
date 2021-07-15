class DinnerPlates:

    def __init__(self, capacity: int):
        self.h = [0]
        self.counter = 0
        self.stacks = [[]]
        self.cap = capacity
        

    def push(self, val: int) -> None:
        if self.h:
            i = heapq.heappop(self.h)
            if i >=len(self.stacks):
                self.push(val)
            else:
                self.stacks[i].append(val)
            if len(self.stacks[i]) <self.cap:
                heapq.heappush(self.h, i)

        else:
            self.stacks.append([val])
            if len(self.stacks[-1]) <self.cap:
                heapq.heappush(self.h, len(self.stacks)-1)
        

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if self.stacks:
            return self.stacks[-1].pop()
        return -1
        

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1
        if len(self.stacks[index]) == self.cap:
            heapq.heappush(self.h, index)
        if self.stacks[index]:
            return self.stacks[index].pop()
        return -1
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


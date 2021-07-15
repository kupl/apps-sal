class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.q = []
        self.stacks = []

    def push(self, val: int) -> None:
        # 1) self.q: is there is available leftmost index
        # 2) is leftmost index less than current size of stacks
        # 3) is leftmost index full
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            heappop(self.q)
        
        if not self.q:
            heappush(self.q, len(self.stacks))
        if self.q[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.q[0]].append(val)
            

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return -1
        return self.popAtStack(len(self.stacks)-1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heappush(self.q, index)
            return self.stacks[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


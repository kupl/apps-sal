class DinnerPlates:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.stacks = []

    def push(self, val):
        while self.queue and self.queue[0] < len(self.stacks) and len(self.stacks[self.queue[0]]) == self.capacity:
            heapq.heappop(self.queue)

        if not self.queue:
            heapq.heappush(self.queue, len(self.stacks))

        if self.queue[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.queue[0]].append(val)

    def pop(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.queue, index)
            return self.stacks[index].pop()
        return -1
        

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


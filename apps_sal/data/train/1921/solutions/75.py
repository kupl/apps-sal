class DinnerPlates:

    def __init__(self, capacity: int):
        self.q = []  # avaliable index for stack
        self.stacks = []  # a list of stack
        self.c = capacity

    def push(self, val: int) -> None:
        # find left most empty stack
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            heapq.heappop(self.q)  # remove index of full stack

        if not self.q:
            heapq.heappush(self.q, len(self.stacks))
        if self.q[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.q[0]].append(val)

    def pop(self) -> int:
        # find right most
        while self.stacks and not self.stacks[-1]:  # remove empty stack
            self.stacks.pop()
        if self.stacks and self.stacks[-1]:
            return self.popAtStack(len(self.stacks) - 1)
        else:
            return -1

    def popAtStack(self, index: int) -> int:
        if index >= 0 and index < len(self.stacks) and self.stacks[index]:
            # if len(self.stacks[index]) == self.c:
            if True:
                heapq.heappush(self.q, index)  # add avalible index
            # print(self.q)
            return self.stacks[index].pop()
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

class DinnerPlates:

    def __init__(self, capacity: int):
        self.q = []
        self.stacks = []
        self.c = capacity

    def push(self, val: int) -> None:
        while self.q and self.q[0] < len(self.stacks) and (len(self.stacks[self.q[0]]) == self.c):
            heapq.heappop(self.q)
        if not self.q:
            heapq.heappush(self.q, len(self.stacks))
        if self.q[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.q[0]].append(val)

    def pop(self) -> int:
        while self.stacks and (not self.stacks[-1]):
            self.stacks.pop()
        if self.stacks and self.stacks[-1]:
            return self.popAtStack(len(self.stacks) - 1)
        else:
            return -1

    def popAtStack(self, index: int) -> int:
        if index >= 0 and index < len(self.stacks) and self.stacks[index]:
            if len(self.stacks[index]) == self.c:
                heapq.heappush(self.q, index)
            return self.stacks[index].pop()
        else:
            return -1

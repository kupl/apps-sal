class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.heap = []
        self.stacks = []

    def push(self, val: int) -> None:
        while self.heap and self.heap[0] < len(self.stacks) and (len(self.stacks[self.heap[0]]) == self.capacity):
            heapq.heappop(self.heap)
        if not self.heap:
            heapq.heappush(self.heap, len(self.stacks))
        if self.heap[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.heap[0]].append(val)

    def pop(self) -> int:
        while self.stacks and (not self.stacks[-1]):
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index >= 0 and index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.heap, index)
            return self.stacks[index].pop()
        return -1

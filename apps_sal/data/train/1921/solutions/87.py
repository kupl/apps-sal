class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks = []
        self.heap = []

    def push(self, val: int) -> None:
        if self.heap and self.heap[0] >= len(self.stacks):
            self.heap = []
        if self.heap:
            if len(self.stacks[self.heap[0]]) < self.cap:
                self.stacks[self.heap[0]].append(val)
                if len(self.stacks[self.heap[0]]) == self.cap:
                    heapq.heappop(self.heap)
        else:
            self.stacks.append([val])
            if self.cap != 1:
                heapq.heappush(self.heap, len(self.stacks) - 1)

    def pop(self) -> int:
        if not self.stacks:
            return -1
        while self.stacks and (not self.stacks[-1]):
            self.stacks.pop()
        if self.stacks and len(self.stacks[-1]) == self.cap:
            heapq.heappush(self.heap, len(self.stacks) - 1)
        return self.stacks[-1].pop() if self.stacks else -1

    def popAtStack(self, index: int) -> int:
        if len(self.stacks) <= index or not self.stacks[index]:
            return -1
        if len(self.stacks[index]) == self.cap:
            heapq.heappush(self.heap, index)
        return self.stacks[index].pop()

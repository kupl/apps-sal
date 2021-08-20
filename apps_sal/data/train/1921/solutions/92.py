class DinnerPlates:

    def __init__(self, capacity: int):
        self.max = capacity
        self.top = 0
        self.stack = collections.defaultdict(list)
        self.stack[self.top] = [0, []]
        self.h = []
        heapq.heappush(self.h, 0)

    def push(self, val: int) -> None:
        ptr = heapq.heappop(self.h)
        self.stack[ptr][1].append(val)
        self.stack[ptr][0] += 1
        if self.stack[ptr][0] < self.max:
            heapq.heappush(self.h, ptr)
        elif ptr == self.top:
            self.top += 1
            self.stack[self.top] = [0, []]
            heapq.heappush(self.h, self.top)

    def popAtStack(self, index: int) -> int:
        if not index in self.stack or not self.stack[index][0]:
            return -1
        if self.stack[index][0] == self.max:
            heapq.heappush(self.h, index)
        self.stack[index][0] -= 1
        return self.stack[index][1].pop()

    def pop(self) -> int:
        while self.top and (not self.stack[self.top][0]):
            self.top -= 1
        return self.popAtStack(self.top)

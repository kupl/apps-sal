from heapq import heappop, heappush


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.pop_q = []
        self.push_q = []

    def push(self, val: int) -> None:
        if self.pop_q:
            i = heappop(self.pop_q)
            self.stack[i] = val
        else:
            i = len(self.stack)
            self.stack.append(val)
        heappush(self.push_q, -i)

    def pop(self) -> int:
        if self.push_q:
            i = -heappop(self.push_q)
            while self.stack[i] == -1 and self.push_q:
                i = -heappop(self.push_q)
            if self.stack[i] != -1:
                heappush(self.pop_q, i)
                val = self.stack[i]
                self.stack[i] = -1
                return val
        return -1

    def popAtStack(self, index: int) -> int:
        start = index * self.capacity
        end = min(start + self.capacity - 1, len(self.stack) - 1)
        for i in range(end, start - 1, -1):
            if self.stack[i] != -1:
                heappush(self.pop_q, i)
                val = self.stack[i]
                self.stack[i] = -1
                return val
        return -1

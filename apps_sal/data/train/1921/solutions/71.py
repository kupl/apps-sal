import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = []
        self.cap = capacity
        self.idx = []

    def push(self, val: int) -> None:
        if len(self.idx) > 0:
            while len(self.idx) > 0:
                i = heappop(self.idx)
                if i < len(self.stack):
                    self.stack[i] = val
                    return
        self.stack.append(val)

    def pop(self) -> int:
        n = len(self.stack) - 1
        if n < 0:
            return -1
        while n > -1:
            if self.stack[n] != -1:
                v = self.stack[n]
                self.stack[n] = -1
                heappush(self.idx, n)
                return v
            else:
                del self.stack[n]
            n -= 1
        return -1

    def popAtStack(self, index: int) -> int:
        count = len(self.stack) // self.cap
        if index > count:
            return -1
        leftptr = index * self.cap
        rightptr = leftptr + self.cap - 1
        if rightptr > len(self.stack) - 1:
            rightptr = len(self.stack) - 1
        while self.stack[rightptr] == -1 and rightptr >= leftptr:
            rightptr -= 1
        if rightptr >= leftptr:
            v = self.stack[rightptr]
            self.stack[rightptr] = -1
            heappush(self.idx, rightptr)
            return v
        else:
            return -1

class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.s = []
        self.h = []

    def push(self, val: int) -> None:
        while self.h and self.h[0] < len(self.s) and (len(self.s[self.h[0]]) == self.c):
            heapq.heappop(self.h)
        if not self.h:
            heapq.heappush(self.h, len(self.s))
        if self.h[0] == len(self.s):
            self.s.append([])
        self.s[self.h[0]].append(val)

    def pop(self) -> int:
        while self.s and (not self.s[-1]):
            self.s.pop()
        return self.popAtStack(len(self.s) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.s) and self.s[index]:
            heapq.heappush(self.h, index)
            return self.s[index].pop()
        return -1

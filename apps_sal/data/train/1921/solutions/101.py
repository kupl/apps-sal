class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.s = []
        self.q = []

    def push(self, val: int) -> None:
        while self.q and (self.q[0] >= len(self.s) or len(self.s[self.q[0]]) == self.c):
            heapq.heappop(self.q)
        if self.q:
            idx = self.q[0]
            self.s[idx].append(val)
            if len(self.s[idx]) == self.c:
                heapq.heappop(self.q)
        else:
            idx = len(self.s) - 1
            if not self.s or len(self.s[-1]) == self.c:
                idx += 1
                self.s.append([])
            self.s[idx].append(val)

    def pop(self) -> int:
        while self.s and (not self.s[-1]):
            self.s.pop()
        return self.popAtStack(len(self.s) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.s) and self.s[index]:
            heapq.heappush(self.q, index)
            return self.s[index].pop()
        return -1

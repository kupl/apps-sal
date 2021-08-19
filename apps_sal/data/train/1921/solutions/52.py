import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.stk = []
        self.c = capacity
        self.pq = []

    def push(self, val: int) -> None:
        while self.pq and self.pq[0] < len(self.stk) and (len(self.stk[self.pq[0]]) == self.c):
            heapq.heappop(self.pq)
        if len(self.pq) == 0:
            heapq.heappush(self.pq, len(self.stk))
        if self.pq[0] == len(self.stk):
            self.stk.append([])
        self.stk[self.pq[0]].append(val)

    def pop(self) -> int:
        while len(self.stk) > 0 and len(self.stk[-1]) == 0:
            self.stk.pop()
        return self.popAtStack(len(self.stk) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stk) and len(self.stk[index]):
            if len(self.stk[index]) == self.c:
                heapq.heappush(self.pq, index)
            return self.stk[index].pop()
        else:
            return -1

import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.q = []
        self.c = capacity
        self.h = []

    def push(self, val: int) -> None:
        if self.h:
            index = heapq.heappop(self.h)
            if index > len(self.q) - 1:
                self.h = []
                if self.q and self.q[-1] and (len(self.q[-1]) < self.c):
                    self.q[-1] += [val]
                else:
                    self.q.append([val])
            elif self.q[index]:
                self.q[index] += [val]
            else:
                self.q[index] = [val]
        elif self.q and self.q[-1] and (len(self.q[-1]) < self.c):
            self.q[-1] += [val]
        else:
            self.q.append([val])

    def pop(self) -> int:
        while self.q:
            if self.q[-1]:
                item = self.q[-1].pop()
                if not self.q:
                    self.q.pop()
                return item
            else:
                self.q.pop()
        return -1

    def popAtStack(self, index: int) -> int:
        if index > len(self.q) - 1:
            return -1
        if self.q[index]:
            item = self.q[index].pop()
            heapq.heappush(self.h, index)
            return item
        else:
            return -1

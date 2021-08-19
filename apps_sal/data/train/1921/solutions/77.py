class DinnerPlates:

    def __init__(self, capacity: int):
        # use a heap to store all the index whose corresponding list is not full
        self.h = []
        self.m = -1
        self.d = {}
        self.c = capacity

    def push(self, val: int) -> None:
        if len(self.d) == 0 or len(self.h) == 0:
            self.m += 1
            self.h = [self.m]
            self.d[self.m] = []

        key = self.h[0]
        if key > self.m:
            self.m += 1
            self.h = [self.m]
            self.d[self.m] = []

        if key not in self.d:
            self.d[key] = []

        self.d[key].append(val)

        if len(self.d[key]) == self.c:
            heapq.heappop(self.h)

    def pop(self) -> int:

        return self.popAtStack(self.m)

    def popAtStack(self, index: int) -> int:
        if len(self.d) == 0 or index not in self.d or len(self.d[index]) == 0:
            return -1

        res = self.d[index].pop()

        if len(self.d[index]) == self.c - 1:
            heapq.heappush(self.h, index)

        while self.m not in self.d or len(self.d[self.m]) == 0:
            if self.m in self.d:
                self.d.pop(self.m)
            self.m -= 1

            if self.m == -1:
                break

        return res

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

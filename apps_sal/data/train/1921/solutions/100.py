import heapq


class DinnerPlates:

    def __init__(self, capacity: int):

        self.q = []
        self.c = capacity
        self.h = []

    def push(self, val: int) -> None:
        # print(\"Before Push: q:{}, h:{}\".format(self.q, self.h))
        if self.h:
            index = heapq.heappop(self.h)
            if index > len(self.q) - 1:
                self.h = []
                if self.q and self.q[-1] and len(self.q[-1]) < self.c:
                    self.q[-1] += [val]
                else:
                    self.q.append([val])
            else:
                if self.q[index]:
                    self.q[index] += [val]
                else:
                    self.q[index] = [val]
        else:
            if self.q and self.q[-1] and len(self.q[-1]) < self.c:
                self.q[-1] += [val]
            else:
                self.q.append([val])
        # print(\"after Push: q:{}, h:{}\".format(self.q, self.h))

    def pop(self) -> int:
        # print(\"POP q:{}\".format(self.q))
        while self.q:
            if self.q[-1]:
                item = self.q[-1].pop()
                if not self.q:
                    self.q.pop()
                # print(\"POP return q:{}, item:{}\".format(self.q, item))
                return item
            else:
                self.q.pop()
        return -1

    def popAtStack(self, index: int) -> int:

        # print(\"Index POP: index:{}, q:{}\".format(index, self.q))
        if index > len(self.q) - 1:
            return -1

        if self.q[index]:
            item = self.q[index].pop()
            heapq.heappush(self.h, index)
            return item
        else:
            return -1

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

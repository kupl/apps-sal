import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.vacancy = []
        self.stacks = []
        self.maxidx = -1

    def push(self, val: int) -> None:
        if self.vacancy:
            pos = self.vacancy[0]
            self.stacks[pos].append(val)
            if len(self.stacks[pos]) == self.capacity:
                heapq.heappop(self.vacancy)
        else:
            pos = len(self.stacks)
            self.stacks.append([])
            self.stacks[pos].append(val)
            if self.capacity > 1:
                heapq.heappush(self.vacancy, pos)
        self.maxidx = max(self.maxidx, pos)

    def pop(self) -> int:
        rangemax = self.maxidx
        for i in range(rangemax, -1, -1):
            if self.stacks[i] != []:
                self.maxidx = i
                x = self.stacks[i].pop()
                if len(self.stacks[i]) == self.capacity - 1:
                    heapq.heappush(self.vacancy, i)
                return x
        else:
            return -1

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or self.stacks[index] == []:
            return -1
        if len(self.stacks[index]) == self.capacity:
            heapq.heappush(self.vacancy, index)
            return self.stacks[index].pop()
        else:
            return self.stacks[index].pop()


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

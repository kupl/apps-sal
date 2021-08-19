class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = []
        self.leftmost = [0]
        self.rightmost = []
        self.capacity = capacity
        self.leftmostset = set([0])
        self.rightmostset = set()

    def push(self, val: int) -> None:
        idx = self.leftmost[0]
        if idx >= len(self.stack):
            self.stack.append([val])
        else:
            self.stack[idx].append(val)
        if len(self.stack[idx]) == self.capacity:
            heapq.heappop(self.leftmost)
            self.leftmostset.remove(idx)
        if len(self.leftmost) == 0:
            heapq.heappush(self.leftmost, idx + 1)
            self.leftmostset.add(idx + 1)
        if idx * -1 not in self.rightmostset:
            heapq.heappush(self.rightmost, idx * -1)
            self.rightmostset.add(idx * -1)

    def pop(self) -> int:
        if len(self.rightmost) == 0:
            return -1
        idx = self.rightmost[0] * -1
        val = self.stack[idx].pop()
        if len(self.stack[idx]) == 0:
            heapq.heappop(self.rightmost)
            self.rightmostset.remove(idx * -1)
        if idx not in self.leftmostset:
            heapq.heappush(self.leftmost, idx)
            self.leftmostset.add(idx)
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stack) or len(self.stack[index]) == 0:
            return -1
        val = self.stack[index].pop()
        if len(self.stack[index]) == 0:
            self.rightmostset.remove(index * -1)
            self.rightmost.remove(index * -1)
        if index not in self.leftmostset:
            heapq.heappush(self.leftmost, index)
            self.leftmostset.add(index)
        return val

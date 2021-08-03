from collections import deque
import heapq


class DinnerPlates:

    def __init__(self, capacity):
        self.capacity = capacity
        self.plates = deque([deque([], maxlen=capacity)])
        self.popHeap = []
        self.pushHeap = [0]

    def push(self, val: int) -> None:
        while self.pushHeap and (self.pushHeap[0] >= len(self.plates) or len(self.plates[self.pushHeap[0]]) == self.capacity):
            heapq.heappop(self.pushHeap)
        if not self.pushHeap:
            self.plates.append(deque(maxlen=self.capacity))
            self.pushHeap = [len(self.plates) - 1]
        i = self.pushHeap[0]
        self.plates[i].append(val)
        heapq.heappush(self.popHeap, -i)
        return

    def pop(self) -> int:
        while self.popHeap and (-self.popHeap[0] >= len(self.plates) or len(self.plates[-self.popHeap[0]]) == 0):
            heapq.heappop(self.popHeap)
        if not self.popHeap:
            return -1
        i = -self.popHeap[0]
        return self.plates[i].pop()

    def popAtStack(self, index: int) -> int:
        if index >= len(self.plates) or not self.plates[index]:
            return -1
        val = self.plates[index].pop()
        if self.plates[index]:
            heapq.heappush(self.popHeap, -index)
        heapq.heappush(self.pushHeap, index)
        return val

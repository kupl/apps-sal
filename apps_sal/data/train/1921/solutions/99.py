class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minHeap = []
        self.stacksTotal = []

    def push(self, val: int) -> None:
        while self.minHeap and self.minHeap[0] < len(self.stacksTotal) and len(self.stacksTotal[self.minHeap[0]]) == self.capacity:
            heapq.heappop(self.minHeap)

        if not self.minHeap:
            heapq.heappush(self.minHeap, len(self.stacksTotal))

        if self.minHeap[0] == len(self.stacksTotal):
            self.stacksTotal.append([])

        self.stacksTotal[self.minHeap[0]].append(val)

    def pop(self) -> int:
        while self.stacksTotal and not self.stacksTotal[-1]:
            self.stacksTotal.pop()

        return self.popAtStack(len(self.stacksTotal) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacksTotal) and self.stacksTotal[index]:
            heapq.heappush(self.minHeap, index)
            return self.stacksTotal[index].pop()

        return -1

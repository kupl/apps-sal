class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = [[]]
        self.cap = capacity
        self.heap = [0]

    def push(self, val: int) -> None:
        while self.heap and self.heap[0] < len(self.stack) and (len(self.stack[self.heap[0]]) == self.cap):
            heapq.heappop(self.heap)
        if not self.heap:
            heapq.heappush(self.heap, len(self.stack))
        if self.heap[0] >= len(self.stack):
            self.stack.append([])
        self.stack[self.heap[0]].append(val)

    def pop(self) -> int:
        while self.stack and (not self.stack[-1]):
            self.stack.pop()
        if not self.stack:
            return -1
        res = self.stack[-1].pop()
        heapq.heappush(self.heap, len(self.stack) - 1)
        return res

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stack) or not self.stack[index]:
            return -1
        heapq.heappush(self.heap, index)
        return self.stack[index].pop()

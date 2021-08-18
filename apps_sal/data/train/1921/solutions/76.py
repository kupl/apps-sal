class DinnerPlates:

    def __init__(self, capacity: int):
        self.arr = [[]]
        self.indices = [0]
        self.cap = capacity

    def push(self, val: int) -> None:
        while len(self.arr[self.indices[0]]) == self.cap:
            heapq.heappop(self.indices)

        self.arr[self.indices[0]].append(val)
        if len(self.arr[self.indices[0]]) == self.cap and self.indices[0] == len(self.arr) - 1:
            heapq.heappush(self.indices, len(self.arr))
            self.arr.append([])

    def pop(self) -> int:
        while self.arr and not self.arr[-1]:
            self.arr.pop()

        if self.arr:
            heapq.heappush(self.indices, len(self.arr) - 1)
            return self.arr[-1].pop()
        else:
            return -1

    def popAtStack(self, index: int) -> int:
        if index >= len(self.arr) or not self.arr[index]:
            return -1
        heapq.heappush(self.indices, index)
        return self.arr[index].pop()

import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.heap = []
        self.plates = []
        self.capacity = capacity
        self.current = None

    def push(self, val: int) -> None:
        if len(self.heap) == 0:
            if len(self.plates) == 0 or len(self.plates[-1]) == self.capacity:
                self.plates.append([])
            self.plates[-1].append(val)
            self.current = len(self.plates) - 1
        else:
            p = heapq.heappop(self.heap)
            self.plates[p].append(val)

    def pop(self) -> int:
        for i in range(self.current, -1, -1):
            if len(self.plates[i]) != 0:
                self.current = i
                return self.plates[i].pop()
            self.current = 0
        return -1

    def popAtStack(self, index: int) -> int:
        if len(self.plates) - 1 < index or len(self.plates[index]) == 0:
            return -1
        p = self.plates[index].pop()
        heappush(self.heap, index)
        return p

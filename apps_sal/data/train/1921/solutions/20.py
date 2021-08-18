class DinnerPlates:

    def __init__(self, capacity: int):
        self.slots = []
        self.capacity = capacity
        self.plates = []
        self.end = -1

    def push(self, val: int) -> None:
        if len(self.slots) == 0:
            self.plates.append([])
            self.plates[-1].append(val)
            self.slots += [len(self.plates) - 1] * (self.capacity - 1)
        else:
            self.plates[heappop(self.slots)].append(val)

        self.end = max(self.end, len(self.plates) - 1)

    def pop(self) -> int:
        if self.end < 0:
            return -1

        return self.popAtStack(self.end)

    def popAtStack(self, index: int) -> int:
        if index >= len(self.plates) or len(self.plates[index]) == 0:
            return -1

        ret = self.plates[index].pop()
        heappush(self.slots, index)

        while self.end >= 0 and len(self.plates[self.end]) == 0:
            self.end -= 1

        return ret

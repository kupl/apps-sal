class DinnerPlates:

    def __init__(self, capacity: int):
        self.data = [[]]
        self.cap = capacity
        self.i = 0

    def push(self, val: int) -> None:
        self.data[self.i].append(val)
        while self.i < len(self.data) and len(self.data[self.i]) == self.cap:
            self.i += 1
        if self.i == len(self.data):
            self.data.append([])

    def pop(self) -> int:
        while self.data and (not self.data[-1]):
            self.data.pop()
        if self.data:
            if len(self.data) <= self.i:
                self.i -= 1
            return self.data[-1].pop()
        return -1

    def popAtStack(self, index: int) -> int:
        if index < len(self.data) and self.data[index]:
            if index < self.i:
                self.i = index
            return self.data[index].pop()
        return -1

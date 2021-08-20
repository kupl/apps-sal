class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = list()
        self.RMNE = -1
        self.LMNF = -1

    def push(self, val: int) -> None:
        if self.LMNF < 0 or self.LMNF >= len(self.stacks):
            self.stacks.append([val])
            self.RMNE = len(self.stacks)
            if self.capacity > 1:
                self.LMNF = len(self.stacks) - 1
        else:
            if len(self.stacks[self.LMNF]) == self.capacity:
                self.LMNF += 1
                self.push(val)
                return
            self.stacks[self.LMNF].append(val)
            if self.RMNE < self.LMNF:
                self.RMNE = self.LMNF
            if len(self.stacks[self.LMNF]) == self.capacity:
                self.LMNF += 1

    def pop(self) -> int:
        if self.RMNE >= len(self.stacks):
            self.RMNE = len(self.stacks) - 1
        while self.RMNE >= 0 and (not self.stacks[self.RMNE]):
            self.RMNE -= 1
            self.stacks.pop()
        if self.RMNE < 0:
            return -1
        val = self.stacks[self.RMNE].pop()
        if self.LMNF > self.RMNE:
            self.LMNF = self.RMNE
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1
        if len(self.stacks[index]) == 0:
            return -1
        val = self.stacks[index].pop()
        if self.LMNF > index or self.LMNF < 0:
            self.LMNF = index
        return val

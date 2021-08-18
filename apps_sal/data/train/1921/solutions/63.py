class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = [[[], capacity]]
        self.openSlot = [0]
        self.capacity = capacity

    def insertAt(self, x):
        l = 0
        r = len(self.openSlot) - 1
        if x < self.openSlot[l]:
            return 0
        if x > self.openSlot[r]:
            return l + 1
        while r > l:
            m = (r + l) // 2
            if self.openSlot[m] < x:
                l = m + 1
            else:
                r = m
        return l

    def push(self, val: int) -> None:
        stackIndex = self.openSlot[0]
        self.stack[stackIndex][0].append(val)
        self.stack[stackIndex][1] -= 1
        if self.stack[stackIndex][1] == 0:
            self.openSlot.pop(0)
        if self.openSlot == []:
            self.stack.append([[], self.capacity])
            self.openSlot.append(len(self.stack) - 1)

    def pop(self) -> int:
        while self.stack != [] and self.stack[-1][1] == self.capacity:
            self.stack.pop(-1)
            self.openSlot.pop(-1)
        if self.stack == []:
            self.stack.append([[], self.capacity])
            self.openSlot.append(len(self.stack) - 1)
            return -1
        poppedVal = self.stack[-1][0].pop(-1)
        self.stack[-1][1] += 1
        if self.stack[-1][1] == 1:
            self.openSlot.insert(len(self.openSlot) - 1, len(self.stack) - 2)
        return poppedVal

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stack) or self.stack[index][0] == []:
            return -1
        poppedVal = self.stack[index][0].pop(-1)
        self.stack[index][1] += 1
        if self.stack[index][1] == 1:
            self.openSlot.insert(self.insertAt(index), index)
        return poppedVal

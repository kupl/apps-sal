class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.s = [[]]
        self.cl = 0
        self.cr = 0

    def push(self, val: int) -> None:
        while self.cl < len(self.s) and len(self.s[self.cl]) == self.c:
            self.cl += 1
        if self.cl == len(self.s):
            self.s.append([])
        self.s[self.cl].append(val)

        if self.cl > self.cr:
            self.cr = self.cl

    def pop(self) -> int:

        while self.cr > 0 and not len(self.s[self.cr]):
            self.s.pop()
            self.cr -= 1
        if self.cr < self.cl:
            self.cl = self.cr

        if len(self.s[self.cr]) > 0:
            return self.s[self.cr].pop()
        return -1

    def popAtStack(self, index: int) -> int:
        if index < len(self.s):
            if len(self.s[index]) > 0:
                t = self.s[index].pop()
                if index < self.cl:
                    self.cl = index
                return t
        return -1

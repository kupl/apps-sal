class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        (self.l, self.r, self.cnt) = (0, 0, 0)
        self.dic = {}
        self.dic[0] = []

    def push(self, val: int) -> None:
        while self.l in self.dic and len(self.dic[self.l]) == self.c:
            self.l += 1
        if self.l not in self.dic:
            self.dic[self.l] = []
        self.dic[self.l].append(val)
        self.cnt += 1
        self.r = max(self.l, self.r)

    def pop(self) -> int:
        if not self.cnt:
            return -1
        while self.r >= 0 and (not self.dic[self.r]):
            self.r -= 1
        self.cnt -= 1
        self.l = min(self.l, self.r)
        return self.dic[self.r].pop()

    def popAtStack(self, index: int) -> int:
        if index not in self.dic or not self.dic[index]:
            return -1
        self.cnt -= 1
        self.l = min(self.l, index)
        return self.dic[index].pop()

class DinnerPlates:

    def __init__(self, capacity: int):
        self.s = [[]]
        self.c = capacity
        self.head = 0  # leftmost unfilled array index
        self.tail = 0  # righmost non-empty array index

    def push(self, val: int) -> None:
        i = 0
        self.s[self.head].append(val)
        self.tail = max(self.head, self.tail)

        while self.head < len(self.s) and len(self.s[self.head]) == self.c:
            self.head += 1
        if self.head == len(self.s):
            self.s.append([])
        # self.tail = max(self.)

    def pop(self) -> int:
        if 0 <= self.tail < len(self.s):
            res = self.s[self.tail].pop()
            while self.tail >= 0 and len(self.s[self.tail]) == 0:
                self.tail -= 1
            return res

        return -1

    def popAtStack(self, index: int) -> int:
        if index >= len(self.s):
            return -1
        if not self.s[index]:
            return -1
        res = self.s[index].pop()
        self.head = min(index, self.head)
        while self.tail > 0 and len(self.s[self.tail]) == 0:
            self.tail -= 1
        return res


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

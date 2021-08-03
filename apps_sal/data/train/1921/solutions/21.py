from collections import deque as dq
import bisect as bs


class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nFull = []
        self.cur = []

    def push(self, val: int) -> None:
        # print(\"push\", val, self.cur, self.nFull)
        if self.nFull:
            self.cur[self.nFull[0]].append(val)
            if len(self.cur[self.nFull[0]]) == self.cap:
                self.nFull.pop(0)
        else:
            self.cur.append([val])
            if len(self.cur[-1]) < self.cap:
                self.nFull.append(len(self.cur) - 1)

    def pop(self) -> int:
        # print(\"pop\", self.cur, self.nFull)
        if not self.cur:
            return -1
        tmp = self.cur[-1].pop()
        if len(self.cur[-1]) == self.cap - 1:
            if self.cur[-1]:
                self.nFull.append(len(self.cur) - 1)
            else:
                self.cur.pop()
        while self.cur and not self.cur[-1]:
            self.cur.pop()
            self.nFull.pop()
        return tmp

    def popAtStack(self, index: int) -> int:
        # print(\"popAt\", index, self.cur, self.nFull)
        if index >= len(self.cur):
            return -1
        if self.cur[index]:
            tmp = self.cur[index].pop()
            if len(self.cur[index]) == self.cap - 1:
                if self.cur[index]:
                    bs.insort(self.nFull, index)
                else:
                    if index == len(self.cur) - 1:
                        self.cur.pop()
                        while self.cur and not self.cur[-1]:
                            self.cur.pop()
                            self.nFull.pop()
                    else:
                        bs.insort(self.nFull, index)
            return tmp
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

from collections import deque
import heapq

class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacklist = []
        self.minh = []

    def push(self, val: int) -> None:
        while len(self.minh) > 0:
            lms = heapq.heappop(self.minh)
            if len(self.stacklist) - 1 >= lms:
                self.stacklist[lms].append(val)
                break
        else:
            if len(self.stacklist) == 0 or len(self.stacklist[-1]) >= self.capacity:
                self.stacklist.append(deque())
            self.stacklist[-1].append(val)

    def pop(self) -> int:
        if len(self.stacklist) == 0:
            return -1

        while len(self.stacklist[-1]) == 0:
            del self.stacklist[-1]

        if len(self.stacklist) > 0:
            res = self.stacklist[-1].pop()
        else:
            res = -1

        if len(self.stacklist[-1]) == 0:
            del self.stacklist[-1]

        return res

    def popAtStack(self, index: int) -> int:
        if len(self.stacklist) - 1 < index or len(self.stacklist[index]) == 0:
            return -1
        else:
            res = self.stacklist[index].pop()
            heapq.heappush(self.minh, index)
            return res


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


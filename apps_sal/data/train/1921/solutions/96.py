from queue import PriorityQueue


class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks = []
        self.q = PriorityQueue()

    def push(self, val: int) -> None:
        while self.stacks and not self.q.empty():
            idx = self.q.get()
            if idx > len(self.stacks) - 1:
                self.stacks.append([])
            # if len(self.stacks[idx]) == self.cap:
            #     continue
            # else:
            self.stacks[idx].append(val)
            if len(self.stacks[idx]) < self.cap:
                self.q.put(idx)
            return

        if not self.stacks:
            self.stacks = [[val]]
            if len(self.stacks[-1]) < self.cap:
                self.q.put(0)
        elif self.q.empty():
            self.stacks.append([val])
            if len(self.stacks[-1]) < self.cap:
                self.q.put(len(self.stacks) - 1)

    def pop(self) -> int:
        while self.stacks:
            if not self.stacks[-1]:
                del self.stacks[-1]
            else:
                v = self.stacks[-1][-1]
                del self.stacks[-1][-1]
                if len(self.stacks[-1]) == self.cap - 1:
                    self.q.put(len(self.stacks) - 1)
                return v
        return -1

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks):
            l = self.stacks[index]
            if l:
                if len(l) == self.cap:
                    self.q.put(index)
                v = l.pop()
                return v
            else:
                return -1
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

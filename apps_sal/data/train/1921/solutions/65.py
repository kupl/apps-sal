class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = [[]]
        self.stack_num = 1
        self.stack_used = []
        self.stack_used.append(0)
        print(capacity)

    def cleanEmptyTail(self) -> None:
        i = self.stack_num - 1
        while i > 0 and len(self.stacks[i]) == 0 and (len(self.stacks[i - 1]) == 0):
            self.stacks.pop()
            self.stack_used.pop()
            self.stack_num -= 1
            i -= 1

    def push(self, val: int) -> None:
        i = self.stack_used[0]
        self.stacks[i].append(val)
        if len(self.stacks[i]) < self.capacity:
            return
        del self.stack_used[0]
        if len(self.stack_used) == 0:
            self.stacks.append([])
            self.stack_used.append(self.stack_num)
            self.stack_num += 1
        return

    def pop(self) -> int:
        i = self.stack_num - 1
        if len(self.stacks[i]) == 0:
            if i == 0:
                return -1
            self.stacks.pop()
            self.stack_used.pop()
            self.stack_num -= 1
            i = self.stack_num - 1
        val = self.stacks[i].pop()
        if len(self.stack_used) == 0 or self.stack_used[-1] != i:
            self.stack_used.append(i)
        self.cleanEmptyTail()
        return val

    def insertUsed(self, index: int) -> None:
        head = 0
        end = len(self.stack_used) - 1
        while end - head > 1:
            i = (head + end) // 2
            mid_index = self.stack_used[i]
            if mid_index == index:
                return
            if mid_index > index:
                end = i
            else:
                head = i
        if self.stack_used[head] > index:
            self.stack_used.insert(head, index)
            return
        if self.stack_used[head] == index or self.stack_used[end] == index:
            return
        if self.stack_used[end] > index:
            self.stack_used.insert(end, index)
            return
        self.stack_used.append(index)
        return

    def popAtStack(self, index: int) -> int:
        if index >= self.stack_num:
            return -1
        if len(self.stacks[index]) == 0:
            return -1
        val = self.stacks[index].pop()
        self.insertUsed(index)
        self.cleanEmptyTail()
        return val

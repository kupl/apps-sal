import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self._stacks = []
        self._capacity = capacity
        self._start = 0

    def push(self, val: int) -> None:
        stack_idx = self._start
        while stack_idx < len(self._stacks):
            if len(self._stacks[stack_idx]) < self._capacity:
                break
            stack_idx += 1
        self._start = stack_idx
        if stack_idx == len(self._stacks):
            self._stacks.append([])
        self._stacks[stack_idx].append(val)

    def pop(self) -> int:
        while self._stacks and not self._stacks[-1]:
            self._stacks.pop()
        if self._stacks:
            self._start = min(self._start, len(self._stacks[-1]) - 1)
            return self._stacks[-1].pop()
        else:
            return -1

    def popAtStack(self, index: int) -> int:
        if index < len(self._stacks) and self._stacks[index]:
            self._start = min(self._start, index)
            return self._stacks[index].pop()
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

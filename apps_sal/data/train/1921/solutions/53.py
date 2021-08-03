from collections import defaultdict
from heapq import heappush, heappop


class DinnerPlates:

    def __init__(self, capacity: int):
        self.size = capacity
        self.stacks = []
        self.leftmost_available = []  # min_heap

    def push(self, val: int) -> None:
        # clean up available stacks (which are actually unavailable)
        while self.leftmost_available and self.leftmost_available[0] < len(self.stacks) and len(self.stacks[self.leftmost_available[0]]) == self.size:
            heappop(self.leftmost_available)

        # now we are at the leftmost available stack (if any)

        if not self.leftmost_available:
            heappush(self.leftmost_available, len(self.stacks))

        # check if the leftmost available stack exist before, or should we create it
        if self.leftmost_available[0] == len(self.stacks):
            self.stacks.append([])

        self.stacks[self.leftmost_available[0]].append(val)

    def pop(self) -> int:

        # clean up empty stacks
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        # now we are at the rightmost non-empty stack (if any)

        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:

            # !! here we could add duplicate index, but it's ok, since we clean up in the push
            heappush(self.leftmost_available, index)
            return self.stacks[index].pop()

        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity, self.stacks = capacity, [[]]
        self.left = 0
        self.right = 0

    def push(self, val: int) -> None:
        while self.left < len(self.stacks) and len(self.stacks[self.left]) == self.capacity:
            self.left += 1
        if self.left == len(self.stacks):
            self.stacks.append([val])
        else:
            self.stacks[self.left].append(val)

        if self.left >= self.right:
            self.right = self.left

    def pop(self) -> int:
        while self.right > 0 and len(self.stacks[self.right]) == 0:
            self.stacks.pop()
            self.right -= 1
        if self.right < self.left:
            self.left = self.right

        if len(self.stacks[self.right]) == 0:
            return -1

        return self.stacks[self.right].pop()

    def popAtStack(self, index: int) -> int:
        if index > len(self.stacks) or not self.stacks[index]:
            return -1
        if index < self.left:
            self.left = index
        return self.stacks[index].pop()


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

class DinnerPlates(object):

    def __init__(self, capacity):
        (self.capacity, self.stacks) = (capacity, [[]])
        (self.left, self.right) = (0, 0)

    def push(self, val):
        while self.left < len(self.stacks) and len(self.stacks[self.left]) == self.capacity:
            self.left += 1
        if self.left == len(self.stacks):
            self.stacks += ([],)
        self.stacks[self.left] += (val,)
        if self.left > self.right:
            self.right = self.left

    def pop(self):
        while self.right > 0 and (not len(self.stacks[self.right])):
            self.stacks.pop()
            self.right -= 1
        if self.right < self.left:
            self.left = self.right
        return -1 if not len(self.stacks[self.right]) else self.stacks[self.right].pop()

    def popAtStack(self, index):
        if index > len(self.stacks) or not len(self.stacks[index]):
            return -1
        if index < self.left:
            self.left = index
        return self.stacks[index].pop()

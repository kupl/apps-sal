
class DinnerPlates(object):

    def __init__(self, capacity):
        self.capacity, self.stacks = capacity, [[]]
        self.left, self.right = 0, 0

    def push(self, val):
        while self.left < len(self.stacks) and len(self.stacks[self.left]) == self.capacity:
            self.left += 1  # find the leftmost stack with space
        if self.left == len(self.stacks):
            self.stacks += [],  # all our stacks are full, add a new one on the right
        self.stacks[self.left] += val,
        if self.left > self.right:
            self.right = self.left  # update right pointer if needed

    def pop(self):
        while self.right > 0 and not len(self.stacks[self.right]):
            self.stacks.pop()  # clear up any empty stacks on the right
            self.right -= 1
        if self.right < self.left:
            self.left = self.right  # update left pointer if needed
        return -1 if not len(self.stacks[self.right]) else self.stacks[self.right].pop()

    def popAtStack(self, index):
        if index > len(self.stacks) or not len(self.stacks[index]):
            return -1
        if index < self.left:
            self.left = index  # we have an empty space even more left than before
        return self.stacks[index].pop()

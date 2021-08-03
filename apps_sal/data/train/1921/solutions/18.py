class DinnerPlates:

    def __init__(self, capacity):

        self.stacks = []
        self.stack = []
        self.size = capacity
        self.left = 0
        self.right = 0

    def push(self, val):

        # when stack is initially empty
        if not self.stacks:
            self.stack.append(val)
            self.stacks.append(self.stack)
            self.left = 0

        else:
            # find the leftmost stack with size less than capacity to append item
            while self.left < len(self.stacks) and len(self.stacks[self.left]) == self.size:
                self.left += 1
            if self.left == len(self.stacks):
                self.stacks.append([])
                self.stacks[self.left].append(val)
            else:
                self.stacks[self.left].append(val)

            self.right = len(self.stacks) - 1

    def pop(self):

        if not self.stacks:
            return -1

        # find the rightmost non empty stack
        if not self.stacks[self.right]:
            while not self.stacks[self.right] and len(self.stacks) - 1 >= self.right:
                self.stacks.pop(self.right)
                self.right -= 1

        item = self.stacks[self.right].pop()

        # if stack gets empty after pop item, move the pointer for rightmost non empty stack
        if not self.stacks[self.right]:
            self.stacks.pop(self.right)
            self.right -= 1

        return item

    def popAtStack(self, index):

        if len(self.stacks) - 1 < index:
            return -1
        if not self.stacks[index]:
            return -1

        # before popping item from stack at index, update the pointer for leftmost stack with capacity
        if self.stacks[index]:
            if self.left > index:
                self.left = index
        return self.stacks[index].pop()

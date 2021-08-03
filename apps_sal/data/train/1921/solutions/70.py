class DinnerPlates:

    def __init__(self, capacity):

        self.stacks = []
        self.stack = []
        self.capacity = capacity
        self.left = 0
        self.right = 0

    def push(self, val):
        # when stack is initially empty
        if not self.stacks:
            self.stack.append(val)
            self.stacks.append(self.stack)
            self.left = 0
        else:
            # find the leftmost stack with capacity less than capacity to append item
            while self.left < len(self.stacks) and len(self.stacks[self.left]) == self.capacity:
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

    # self made, TLE
#     def __init__(self, capacity: int):
#         self.stacks = []
#         self.capacity = capacity

#     def push(self, val: int) -> None:
#         if not self.stacks:
#             self.stacks.append([])
#         for i in range(len(self.stacks)):
#             if len(self.stacks[i]) < self.capacity:
#                 self.stacks[i].append(val)
#                 break
#         else:
#             self.stacks.append([val])

#     def pop(self) -> int:
#         if not self.stacks:
#             return -1
#         pop_val = None
#         for i in range(len(self.stacks) - 1, -1, -1):
#             if self.stacks[i]:
#                 pop_val = self.stacks[i].pop()
#                 if not self.stacks[i]:
#                     del self.stacks[i]
#                 break
#             else:
#                 self.stacks.pop()

#         return pop_val if pop_val else -1

#     def popAtStack(self, index: int) -> int:
#         if index >= len(self.stacks):
#             return -1
#         pop_val = None
#         if self.stacks[index]:
#             pop_val = self.stacks[index].pop()
#         return pop_val if pop_val else -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

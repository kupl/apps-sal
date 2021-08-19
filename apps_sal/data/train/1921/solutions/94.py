class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = [[]]
        self.capacity = capacity
        self.left = 0
        self.right = -1

    def push(self, val: int) -> None:
        self.stacks[self.left].append(val)
        if self.left > self.right:
            self.right = self.left
        if len(self.stacks[self.left]) == self.capacity:
            self.left = self.left + 1
            while True:
                if self.left <= len(self.stacks) - 1:
                    if len(self.stacks[self.left]) < self.capacity:
                        return None
                    else:
                        self.left = self.left + 1
                else:
                    self.stacks.append([])
                    return None

    def pop(self) -> int:
        if self.right == -1:
            return -1
        else:
            toreturn = self.stacks[self.right].pop()
            if self.stacks[self.right]:
                if self.left > self.right:
                    self.left = self.right
                return toreturn
            else:
                self.right = self.right - 1
                while True:
                    if self.right > -1:
                        if self.stacks[self.right]:
                            return toreturn
                        else:
                            self.right = self.right - 1
                    return toreturn

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks):
            if self.stacks[index]:
                if index < self.left:
                    self.left = index
                toreturn = self.stacks[index].pop()
                if not self.stacks[index] and index == self.right:
                    self.right = self.right - 1
                while True:
                    if self.right > -1:
                        if self.stacks[self.right]:
                            return toreturn
                        else:
                            self.right = self.right - 1
                    return toreturn
        return -1

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = [[]]
        self.leftmost = 0
        self.rightmost = 0
        

    def push(self, val: int) -> None:
        try:
            self._find_leftmost()
        except IndexError:
            self.stack.append([])
\t\t\t# updates the rightmost index if needed
            if self.leftmost >= self.rightmost:
                self.rightmost = self.leftmost

        self.stack[self.leftmost].append(val)
        
    def pop(self) -> int:
        try:
            self._find_rightmost()
        except IndexError:
            self.rightmost = 0
            return -1

        return self.stack[self.rightmost].pop()

    def popAtStack(self, index: int) -> int:

        if index >= len(self.stack) or not self.stack[index]:
            return -1

        value = self.stack[index].pop()
        if index < self.leftmost:
            self.leftmost = index
        return value

    def _find_leftmost(self):
        while len(self.stack[self.leftmost]) >= self.capacity:
            self.leftmost += 1

    def _find_rightmost(self):
        while not self.stack[self.rightmost]:
            self.rightmost -= 1

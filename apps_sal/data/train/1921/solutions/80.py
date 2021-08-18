class DinnerPlates:

    def __init__(self, capacity: int):
        self.indicies = []
        self.stacks = []
        self.cap = capacity

    def clean_stack(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

    def push(self, val: int) -> None:
        while self.indicies:
            index = heappop(self.indicies)

            if index < len(self.stacks) and len(self.stacks[index]) < self.cap:
                self.stacks[index].append(val)
                return

        if self.stacks and len(self.stacks[-1]) < self.cap:
            self.stacks[-1].append(val)
        else:
            self.stacks.append([val])

    def pop(self) -> int:
        if not self.stacks:
            return -1
        else:
            res = self.stacks[-1].pop()

        if not self.stacks[-1]:
            self.clean_stack()
        else:
            heappush(self.indicies, len(self.stacks) - 1)

        return res

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        res = self.stacks[index].pop()

        if not self.stacks[-1]:
            self.clean_stack()
        else:
            heappush(self.indicies, index)

        return res

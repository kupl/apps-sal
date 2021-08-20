class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.available_to_push = []

    def push(self, val: int) -> None:
        while len(self.available_to_push) > 0 and self.available_to_push[0] < len(self.stack) and (len(self.stack[self.available_to_push[0]]) == self.capacity):
            heappop(self.available_to_push)
        if len(self.available_to_push) == 0:
            heappush(self.available_to_push, len(self.stack))
        if self.available_to_push[0] == len(self.stack):
            self.stack.append([])
        self.stack[self.available_to_push[0]].append(val)

    def pop(self) -> int:
        while len(self.stack) > 0 and len(self.stack[-1]) == 0:
            self.stack.pop()
        return self.popAtStack(len(self.stack) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stack) and len(self.stack[index]) > 0:
            heappush(self.available_to_push, index)
            return self.stack[index].pop()
        return -1

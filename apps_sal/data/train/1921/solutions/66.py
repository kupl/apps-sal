class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack_list = []
        self.available_stacks = []

    def push(self, val: int) -> None:
        self.remove_empty_stacks_at_the_end()
        if not self.available_stacks:
            self.stack_list.append([])
            self.available_stacks.append(len(self.stack_list) - 1)
        first_available_stack = self.available_stacks[0]
        self.stack_list[first_available_stack].append(val)
        if len(self.stack_list[first_available_stack]) == self.capacity:
            heapq.heappop(self.available_stacks)

    def remove_empty_stacks_at_the_end(self):
        while self.stack_list and (not self.stack_list[-1]):
            self.stack_list.pop()
        while self.available_stacks and self.available_stacks[0] >= len(self.stack_list):
            heapq.heappop(self.available_stacks)

    def pop(self) -> int:
        self.remove_empty_stacks_at_the_end()
        return self.popAtStack(len(self.stack_list) - 1)

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stack_list) or (not self.stack_list[index]):
            return -1
        if len(self.stack_list[index]) == self.capacity:
            heapq.heappush(self.available_stacks, index)
        result = self.stack_list[index].pop()
        self.remove_empty_stacks_at_the_end()
        return result

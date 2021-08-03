class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stack = []
        self.available_to_push = []   # min heap to store the idx of available-to-push stack

    def push(self, val: int) -> None:       # O(logn)
        # step 1: pop out all the left stacks that are not avaliable to push,
        # so that after the while loop, we will know the leftmost stack that is available to push
        while len(self.available_to_push) > 0 and self.available_to_push[0] < len(self.stack) and len(self.stack[self.available_to_push[0]]) == self.capacity:
            heappop(self.available_to_push)

        # if the q is empty, meaning there are no more available stacks
        if len(self.available_to_push) == 0:
            heappush(self.available_to_push, len(self.stack))
        if self.available_to_push[0] == len(self.stack):
            self.stack.append([])

        # finally, we can push our val into the leftmost available stack
        self.stack[self.available_to_push[0]].append(val)

    def pop(self) -> int:       # O(1)
        # step 1: pop out all the empty stacks on the right, cuz they are not available to pop
        while len(self.stack) > 0 and len(self.stack[-1]) == 0:
            self.stack.pop()

        return self.popAtStack(len(self.stack) - 1)

    def popAtStack(self, index: int) -> int:        # O(logn)
        # check if it is available to pop
        if 0 <= index < len(self.stack) and len(self.stack[index]) > 0:
            heappush(self.available_to_push, index)     # add this index to the available-to-push heap
            return self.stack[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

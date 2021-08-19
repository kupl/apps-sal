import heapq


class DinnerPlates:
    def __init__(self, capacity: int):
        # record values of all stack of plates, its last nonempty stack are the rightmost position
        self.stk = []
        self.c = capacity
        # record the available stack, will use heap to quickly find the smallest available stack
        self.pq = []

    def push(self, val: int) -> None:
        # Time: O(logN)
        # To push, we need to find the leftmost available position. first, let's remove any stacks on the left that are full
        while self.pq and self.pq[0] < len(self.stk) and len(self.stk[self.pq[0]]) == self.c:
            heapq.heappop(self.pq)

        # if the q is empty, meaning there are no more available stacks
        if len(self.pq) == 0:
            heapq.heappush(self.pq, len(self.stk))

        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.pq[0] == len(self.stk):
            self.stk.append([])

        # append the value to the leftmost available stack
        self.stk[self.pq[0]].append(val)

    def pop(self) -> int:
        # Time: amortized O(1)
        # To pop, we need to find the rightmost nonempty stack
        # 1) stacks is not empty (self.stacks) and
        # 2) the last stack is empty
        while len(self.stk) > 0 and len(self.stk[-1]) == 0:
            self.stk.pop()

        return self.popAtStack(len(self.stk) - 1)

    def popAtStack(self, index: int) -> int:
        # Time: O(logN)
        # To pop from an stack of given index, we need to make sure that it is not empty
        # 1) the index for inserting is valid and，
        # 2) the stack of interest is not empty
        if 0 <= index < len(self.stk) and len(self.stk[index]):
            # we add the index into the available stack
            heapq.heappush(self.pq, index)
            # if len(self.stk[index]) == self.c:
            #     heapq.heappush(self.pq, index)
            # take the top plate, pop it and return its value
            return self.stk[index].pop()
        # otherwise, return -1 because we can't pop any plate
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

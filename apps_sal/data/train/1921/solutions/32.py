# 1172. Dinner Plate Stacks

from heapq import *

class DinnerPlates:
    def __repr__ (self):
        return f'DP ({self.stacks}, {self.nonfull})'
    
    def __init__ (self, capacity):
        self.cap = capacity
        self.stacks = []
        self.nonfull = [] # heap

    def push (self, val):
        # look in self.nonfull first
        while self.nonfull:
            first = self.nonfull [0]
            if first < len (self.stacks) and len (self.stacks[first]) < self.cap:
                self.stacks[first].append (val)
                if len (self.stacks[first]) == self.cap:
                    # no longer nonfull
                    heappop (self.nonfull)
                return
            else:
                heappop (self.nonfull)
        # not found yet
        new_stack = len (self.stacks)
        self.stacks.append ([val])
        if len (self.stacks[new_stack]) < self.cap:
            heappush (self.nonfull, new_stack)

    def pop (self):
        while self.stacks:
            if not self.stacks[-1]:
                self.stacks.pop ()
            else:
                ans = self.stacks[-1].pop ()
                popped_stack = len (self.stacks) - 1
                if not self.stacks[-1]:
                    self.stacks.pop ()
                elif len (self.stacks[-1]) == self.cap - 1:
                    heappush (self.nonfull, popped_stack)
                return ans
        return -1

    def popAtStack (self, index):
        if index >= len (self.stacks):
            return -1
        elif not self.stacks[index]:
            return -1
        else:
            ans = self.stacks[index].pop ()
            if len (self.stacks[index]) == self.cap - 1:
                heappush (self.nonfull, index)
            return ans

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


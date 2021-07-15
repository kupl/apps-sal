class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity #capacity
        self.stacks = [[]] #empty stack with the first stack
        self.stack_num = 1 #total of active (used) stack number
        self.stack_used = [] #order from left to right where there is an empty space
        self.stack_used.append(0) #the first stack is ready
        print(capacity)

    def cleanEmptyTail(self) -> None:
        i = self.stack_num - 1
        while i > 0 and len(self.stacks[i]) == 0 and len(self.stacks[i-1]) == 0:
            self.stacks.pop()
            self.stack_used.pop()
            self.stack_num -= 1
            i -= 1
        
    def push(self, val: int) -> None:
        # assert len(stack_used) > 0, a valid state
        i = self.stack_used[0] # return the left most stack number
        self.stacks[i].append(val)
        if len(self.stacks[i]) < self.capacity:
            # print('push', val)
            # print(self.stacks)
            # print(self.stack_used)
            return
        # now start to check this stack is full
        del self.stack_used[0] # this stack is not available
        if len(self.stack_used) == 0:
            # start to get the next one
            self.stacks.append([])
            self.stack_used.append(self.stack_num)
            self.stack_num += 1
        # print('push', val)
        # print(self.stacks)
        # print(self.stack_used)
        return

    def pop(self) -> int:
        # it's possible the rightmost stack is empty in the algorithm when it is just prepared.
        i = self.stack_num - 1
        if len(self.stacks[i]) == 0: #the algorithm should guarantee that there is not more than two empty
            # we have to remove this stack if it's not the leftmost one.
            if i == 0:
                return -1
            self.stacks.pop()
            self.stack_used.pop()
            self.stack_num -= 1
            i = self.stack_num -1
        # now remove this one from stack
        val = self.stacks[i].pop()
        if len(self.stack_used) == 0 or self.stack_used[-1] != i: 
            self.stack_used.append(i)
        # clean rightmost empty stacks
        self.cleanEmptyTail()
        # return value
        # print('p')
        # print(self.stacks)
        # print(self.stack_used)
        return val
    
    def insertUsed(self, index: int) -> None:
        head = 0
        end = len(self.stack_used) - 1
        while end - head > 1:
            i = (head + end) // 2
            mid_index = self.stack_used[i]
            if mid_index == index: 
                return # already there
            if mid_index > index:
                end = i
            else:
                head = i
        # 5 positions _ head _ end _
        if self.stack_used[head] > index:
            self.stack_used.insert(head, index)
            return
        if self.stack_used[head] == index or self.stack_used[end] == index:
            return
        if self.stack_used[end] > index:
            self.stack_used.insert(end, index)
            return
        self.stack_used.append(index)
        return

    def popAtStack(self, index: int) -> int:
        if index >= self.stack_num:
            return -1
        if len(self.stacks[index]) == 0:
            return -1
        val = self.stacks[index].pop()
        # insert into the stack_used list
        self.insertUsed(index)
        # clean
        self.cleanEmptyTail()
        # print('pAt', index)
        # print(self.stacks)
        # print(self.stack_used)
        return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


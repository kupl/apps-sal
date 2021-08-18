class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = list()
        self.heapnonfull = list()
        self.heapnonempty = list()

    def push(self, val: int) -> None:
        if(len(self.heapnonfull) == 0):
            newlist = list()
            newlist.append(val)
            self.stacks.append(newlist)
            index = len(self.stacks) - 1
            if(self.capacity > 1):
                heappush(self.heapnonfull, index)
            heappush(self.heapnonempty, 0 - index)
        else:
            index = self.heapnonfull[0]
            self.stacks[index].append(val)
            if(len(self.stacks[index]) == self.capacity):
                heappop(self.heapnonfull)

    def pop(self) -> int:

        while(len(self.heapnonempty) > 0 and len(self.stacks[0 - self.heapnonempty[0]]) == 0):
            heappop(self.heapnonempty)
            self.stacks.pop()

        if(len(self.heapnonempty) == 0):
            return -1
        index = 0 - self.heapnonempty[0]
        val = self.stacks[index].pop()
        if(len(self.stacks[index]) == 0):
            heappop(self.heapnonempty)
            self.stacks.pop()
        else:
            if(len(self.stacks[index]) < self.capacity):
                heappush(self.heapnonfull, index)
        return val

    def popAtStack(self, index: int) -> int:
        if(index >= len(self.stacks)):
            return -1

        curlen = len(self.stacks[index])
        if(curlen == 0):
            return -1

        if(curlen - 1 < self.capacity and curlen == self.capacity and index != len(self.stacks) - 1):
            heappush(self.heapnonfull, index)

        return self.stacks[index].pop()

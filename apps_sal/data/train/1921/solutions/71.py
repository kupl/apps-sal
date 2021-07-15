import heapq
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = [] # just one array to simulate all the stacks
        self.cap = capacity 
        self.idx = [] # min-heap to track empty indicies

    def push(self, val: int) -> None:
        if len(self.idx) > 0:
            while len(self.idx) > 0:
                i = heappop(self.idx) 
                # Given that we just push index but don't validate the cache while
                # poping we need to check if this index is within current limits
                if i < len(self.stack):
                    self.stack[i] = val
                    return 
                
        # we didn't find empty spaces so we add to the end
        self.stack.append(val)

    def pop(self) -> int:
        n = len(self.stack) - 1
        if n < 0:
            return -1
        
        while n > -1:
            if self.stack[n] != -1:
                v = self.stack[n]
                self.stack[n] = -1
                # Add the empty index to the heap
                heappush(self.idx , n)
                return v
            else:
                # Because those appear at the end the list we free those memory spaces so
                # later pop operations are optimized
                del(self.stack[n])
            n -= 1
            
        # All stacks are empty
        return -1

    def popAtStack(self, index: int) -> int:
        # additional check that is [optional] just to skip any effort 
        # if index is already out of current limits
        count = len(self.stack) // self.cap
        if index > count:
            return -1
        
        # capture the boundaries of this stack
        leftptr = (index * self.cap) 
        rightptr = leftptr + self.cap - 1
        if rightptr > (len(self.stack) - 1): # edge case
            rightptr = (len(self.stack) - 1)
            
        # traverse within the stack at this index until we empty it or we find an occupied location    
        while self.stack[rightptr] == -1 and rightptr >= leftptr:
            rightptr -=1
            
        # if it isn't empty it means we found occupied position
        if rightptr >= leftptr:
            v = self.stack[rightptr]
            self.stack[rightptr] = -1
            # Add the empty index to the heap
            heappush(self.idx , rightptr)
            return v
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


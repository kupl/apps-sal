class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.stacks = []
        # Prio queue (heap)
        self.h = []

    def push(self, val: int) -> None:
        
        # As we can have multiple time same index in heap, we clean if stack have been fulled
        while self.h and self.h[0] < len(self.stacks) and len(self.stacks[self.h[0]]) == self.c:
            heapq.heappop(self.h)
        
        # Prio queue is empty, we declare a new list, store it's index
        if not self.h:
            heapq.heappush(self.h, len(self.stacks))
        
        #create or re-create new stack (heap can still ref a stack that have been deleted from stacks after multiple pop)
        if self.h[0] == len(self.stacks):
            self.stacks.append([])
        
        self.stacks[self.h[0]].append(val)

    def pop(self) -> int:
        
        # We clean emptied stacks
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        
        return self.popAtStack(len(self.stacks)-1)

    def popAtStack(self, index: int) -> int:
        
        # Can have multiple time same index in the heap (else we would need to check if elem in heap O(n))
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.h, index)
            
            return self.stacks[index].pop()
        return -1
    
    

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


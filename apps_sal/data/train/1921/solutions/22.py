class DinnerPlates(object):

    def __init__(self, capacity):
        \"\"\"
        :type capacity: int
        \"\"\"
        self.stacks = []
        self.cap = capacity
        self.not_full = [] #to push min heap
        self.not_empty = [] #to pop

    def push(self, val):
        \"\"\"
        :type val: int
        :rtype: None
        \"\"\"
        #print(\"push\")
        if self.not_full:
            index = self.not_full[0]
            self.stacks[index].append(val)
            if len(self.stacks[index]) == self.cap:
                heapq.heappop(self.not_full)
                
        else:
            index = len(self.stacks)
            if self.cap > 1: #here
                heapq.heappush(self.not_full, index)
            heapq.heappush(self.not_empty, -index)
            self.stacks += [[val]]
            
    def pop(self):
        \"\"\"
        :rtype: int
        \"\"\"

        #print(\"pop\")
        while self.not_empty and not self.stacks[-self.not_empty[0]]:
            heapq.heappop(self.not_empty)
            self.stacks.pop() #here
            
        if self.not_empty:
            index = -self.not_empty[0]
            val = self.stacks[index].pop()
            if not self.stacks[index]:
                heapq.heappop(self.not_empty)
                self.stacks.pop()
                
            return val
        
        return -1
        
        
        

    def popAtStack(self, index):
        \"\"\"
        :type index: int
        :rtype: int
        \"\"\"
        #print(\"popAt\")
        if index >= 0 and index < len(self.stacks) and self.stacks[index]:
            if len(self.stacks[index]) == self.cap and index != len(self.stacks) - 1:
                heapq.heappush(self.not_full, index)  
            return self.stacks[index].pop()
        
        return -1

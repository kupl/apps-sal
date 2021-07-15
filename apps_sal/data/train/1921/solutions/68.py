class DinnerPlates:

    def __init__(self, capacity: int):
        self.stack = [[]]
        self.heap = [0]
        self.cap = capacity
        
    def push(self, val: int) -> None:
        while self.heap[0]<len(self.stack) and len(self.stack[self.heap[0]])==self.cap:
            heapq.heappop(self.heap)
        
        if self.heap[0]==len(self.stack):
            self.stack.append([])
        self.stack[self.heap[0]].append(val)
        if len(self.stack[self.heap[0]])==self.cap:
            heapq.heappush(self.heap, len(self.stack))
        
    def pop(self) -> int:
        while self.stack and not self.stack[-1]:
            self.stack.pop()
        
        if not self.stack:
            return -1

        heapq.heappush(self.heap, len(self.stack)-1)
        return self.stack[-1].pop()
    
    def popAtStack(self, index: int) -> int:
        if index>=len(self.stack) or not self.stack[index]:
            return -1
        
        heapq.heappush(self.heap, index)
        return self.stack[index].pop()

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


class DinnerPlates:
    #Use heap to store index of available stack
    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks = []
        self.heap = []

    def push(self, val: int) -> None:
        #While exists heap and most left items in the stack that are full -> pop stack 
        while self.heap and self.heap[0] < len(self.stacks) and len(self.stacks[self.heap[0]]) == self.cap:
            heapq.heappop(self.heap)
        
        #If heap is empty -> need to insert in next index
        if not self.heap:
            heapq.heappush(self.heap, len(self.stacks))
        
        #If first item in heap has index == len(stacks) = last_index + 1, need to insert to next [array]
        if self.heap[0] == len(self.stacks):
            self.stacks.append([])
            
        self.stacks[self.heap[0]].append(val)
        
            
    def pop(self) -> int:
        while self.stacks and self.stacks[-1] == []:
            self.stacks.pop()
            
        return self.popAtStack(len(self.stacks)-1)

    def popAtStack(self, index: int) -> int:
        if 0<=index<len(self.stacks) and self.stacks[index] != []:
            heapq.heappush(self.heap, index)
            return self.stacks[index].pop()
        
        return -1
            

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


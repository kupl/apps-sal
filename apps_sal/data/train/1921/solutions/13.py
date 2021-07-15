class DinnerPlates:

    def __init__(self, capacity: int):
        self.rightheap=[]
        self.leftheap=[]
        heapq.heappush(self.leftheap,0)
        self.hashmap=defaultdict(list)
        self.capacity=capacity
        self.ind=0

    def push(self, val: int) -> None:
        slot=self.leftheap[0]
        if len(self.hashmap[slot])==0:
            heapq.heappush(self.rightheap,-slot)
        self.hashmap[slot].append(val)
        if len(self.hashmap[slot])==self.capacity:
            heapq.heappop(self.leftheap)
            
        if len(self.leftheap)==0:
            self.ind+=1
            heapq.heappush(self.leftheap,self.ind)
            
       

    def pop(self) -> int:
        if not self.rightheap:
            return -1
        while(len(self.hashmap[-self.rightheap[0]])==0):
              heapq.heappop(self.rightheap)
        slot=-heapq.heappop(self.rightheap)
        value=self.hashmap[slot].pop()
        if len(self.hashmap[slot])!=0:
            heapq.heappush(self.rightheap,-slot)
        else:
            self.ind=slot-1
        heapq.heappush(self.leftheap,slot)
        
        return value
        

    def popAtStack(self, index: int) -> int:
        if not self.hashmap[index]:
            return -1
        else:
            value=self.hashmap[index].pop()
            if len(self.hashmap[index])+1==self.capacity:
                heapq.heappush(self.leftheap,index)
            return value     
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


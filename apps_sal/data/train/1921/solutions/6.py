import heapq
class DinnerPlates:

    def __init__(self, capacity: int):
        self.heap=[]
        self.plates=[]
        self.capacity=capacity
        self.current=None
    def push(self, val: int) -> None:
        # print(\"push\",val, self.plates)
        if len(self.heap)==0:
            if len(self.plates)==0 or len(self.plates[-1])==self.capacity:
                self.plates.append([])
            self.plates[-1].append(val)
            self.current=len(self.plates)-1

        else:
            p=heapq.heappop(self.heap)
            self.plates[p].append(val)

    def pop(self) -> int:
        # print(\"pop\", self.plates)

        for i in range(self.current,-1,-1):
            if len(self.plates[i])!=0:
                self.current=i
                return self.plates[i].pop()
            self.current=0
        return -1
        # if len(self.plates)==0:
        #     return -1
        # p=self.plates[-1][-1]
        # self.plates[-1].pop()
        # # if len(self.plates[-1])==0:
        # #     self.plates.pop()
        # return p
    def popAtStack(self, index: int) -> int:
    
        # print(\"popAtStack\",index, self.plates)
        if len(self.plates)-1<index or len(self.plates[index])==0:
            return -1
        # 3 3
        p=self.plates[index].pop()
        heappush(self.heap, index)
        return p


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


# 1 2
# 3 3
# 5 5
# 5  
# 6 7




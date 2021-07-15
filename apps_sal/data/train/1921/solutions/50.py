import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.C = capacity
        self.S = [[]]
        self.PQ = [0]
        self.M = 0

    def push(self, val: int) -> None:
        if not self.PQ:
            self.S.append([])
            heapq.heappush(self.PQ, len(self.S)-1)
            
        tmp = heapq.heappop(self.PQ)
        self.M = max(self.M, tmp)
        self.S[tmp].append(val)
        if len(self.S[tmp]) < self.C:
            heapq.heappush(self.PQ, tmp)
        

    def pop(self) -> int:
        tmp = self.M
        while tmp > 0 and not self.S[tmp]:
            tmp -= 1
        self.M = tmp
        if not self.S[tmp]:
            return -1
        if len(self.S[tmp]) == self.C:
            heapq.heappush(self.PQ, tmp)
        return self.S[tmp].pop()
        

    def popAtStack(self, index: int) -> int:
        if len(self.S) > index and self.S[index]:
            if len(self.S[index]) == self.C:
                heapq.heappush(self.PQ, index)
            return self.S[index].pop()
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


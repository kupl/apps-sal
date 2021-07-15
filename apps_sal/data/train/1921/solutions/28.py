import heapq
class DinnerPlates:
    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity
        self.available_pos = []

    def push(self, val: int) -> None:
        if len(self.available_pos) == 0:
            self.cache.append([])
            heapq.heappush(self.available_pos, len(self.cache) - 1)
        min_idx = self.available_pos[0]
        if min_idx >= len(self.cache):
            needed = min_idx + 1 - len(self.cache)
            for _ in range(needed):
                self.cache.append([])
        self.cache[min_idx].append(val)
        if len(self.cache[min_idx]) == self.capacity:
            heapq.heappop(self.available_pos)

    def pop(self) -> int:
        while len(self.cache) > 0 and len(self.cache[-1]) == 0:
            self.cache.pop()
        if len(self.cache) == 0: return -1
        
        val = self.cache[-1].pop()
        # if len(self.cache[-1]) == 0: 
        #     self.cache.pop()
        if len(self.cache[-1]) == self.capacity - 1:
            heapq.heappush(self.available_pos, len(self.cache) - 1)
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.cache) or len(self.cache[index]) == 0: return -1
        val = self.cache[index].pop()
        if len(self.cache[index]) == self.capacity - 1:
            heapq.heappush(self.available_pos, index)
        return val


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)


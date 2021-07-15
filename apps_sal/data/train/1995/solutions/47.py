class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        load = [0] * 1001
        for count, from_idx, to_idx in trips:
            for i in range(from_idx, to_idx):
                load[i] += count
                if load[i] > capacity:
                    return False
        return True

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        import numpy as np
        timestamp = np.zeros(1001)

        for trip in trips:
            timestamp[trip[1]:] += trip[0]
            timestamp[trip[2]:] -= trip[0]

        if max(timestamp) > capacity:
            return False
        return True

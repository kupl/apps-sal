class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        counter = [0] * 1000
        for elem in trips:
            for i in range(elem[1], elem[2]):
                counter[i] += elem[0]
        if max(counter) > capacity:
            return False
        return True

class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        counter = set()
        for i in arr:
            counter.add(i)
        position = 0
        i = 1
        while True:
            if i not in counter:
                position += 1
            if position == k:
                return i
            i += 1

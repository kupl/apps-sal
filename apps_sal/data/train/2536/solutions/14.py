

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1
        for elem in set(arr):
            recurred = [e2 for e2 in arr if e2 == elem]
            if len(recurred) == elem:
                if elem > lucky:
                    lucky = elem
        return lucky

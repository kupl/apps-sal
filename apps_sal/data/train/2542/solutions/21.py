class Solution:

    def isMonotonic(self, a: List[int]) -> bool:
        isIncreasing = isDecreasing = True
        for i in range(len(a) - 1):
            if a[i] < a[i + 1]:
                isIncreasing = False
            if a[i] > a[i + 1]:
                isDecreasing = False
        return isIncreasing or isDecreasing

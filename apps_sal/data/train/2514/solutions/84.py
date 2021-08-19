class Solution:

    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance = [[val - d, val + d] for val in arr1]
        total = 0
        for ran in distance:
            for val in arr2:
                if ran[0] <= val and val <= ran[1]:
                    total += 1
                    break
        return len(arr1) - total

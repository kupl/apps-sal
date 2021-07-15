class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        op = 0
        for i in range(len(arr1)):
            ref = [abs(arr1[i] - a2) <= d for a2 in arr2]
            if sum(ref) == 0:
                op += 1
        return op
    # def findTheDistanceValue(self, A, B, d):
    #     return sum(all(abs(a - b) > d for b in B) for a in A)


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = [0] * 100001
        n = len(arr)
        for i in arr:
            count[i] += 1
        for i in range(len(count)):
            if(count[i] > int(0.25 * n)):
                return i

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 0
        num = arr[0]
        for x in arr:
            if x == num:
                count = count+ 1
            elif x != num and ((count / len(arr))>0.25):
                return num
            else:
                num = x
                count = 1
        return arr[len(arr)-1]

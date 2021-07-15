class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr)//4
        count = 1
        for i in range(len(arr)):
            if i==len(arr)-1:
                return arr[i]
            if arr[i]==arr[i+1]:
                count+=1
                if count>quarter:
                    return arr[i]
            else:
                count=1
                


class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        """
        # fisrt solution
        if len(arr)==1: return arr[0]
        step = 1 if len(arr)<8 else len(arr)//4        
        for i in range(len(arr)):
            if arr[i]==arr[i+step]: return arr[i]
        """
        return max(set(arr), key=arr.count)

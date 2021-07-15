class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int: # good 2, check the diff between idx and element, then compare to k, time O(logn), space O(1)
        l, r = 0, len(arr)-1
        while l<r: # find the first idx whose diff from the num is >=k+1 
            m = (l+r)//2
            if arr[m]-m>=k+1:
                r = m
            else:
                l = m+1
        
        if arr[l]-l < k+1: # cannot find within the range of the arr
            return l+k+1 # arr[l]+(k+1)-(arr[l]-l), l=n-1 actually
        else: # can find
            return l+k # arr[l-1]+(k+1)-(arr[l-1]-l+1)


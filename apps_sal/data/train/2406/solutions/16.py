class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r=0,len(arr)-1
        while(l<=r):
            mid = l + (r - l) // 2; 
            print(mid)
            if(arr[mid-1]<arr[mid]>arr[mid+1]):
                return mid
            elif(arr[mid-1]>arr[mid]):
                r=r-1
            else:
                l=l+1


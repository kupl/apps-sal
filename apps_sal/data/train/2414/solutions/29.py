class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans,n = 0,len(arr)
        for x in range(n-2):
            for y in range(x+1,n-1):
                for z in range(y+1,n):
                    if abs(arr[x]-arr[y])<=a and abs(arr[y]-arr[z])<=b and abs(arr[x]-arr[z])<=c:
                        ans+=1
        return ans

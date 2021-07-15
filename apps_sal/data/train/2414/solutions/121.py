class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt=0
        n=len(arr)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    d1=abs(arr[i]-arr[j])
                    d2=abs(arr[j]-arr[k])
                    d3=abs(arr[k]-arr[i])
                    if (d1<=a) and (d2<=b) and (d3<=c):
                        cnt+=1
        return cnt

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
        count=0
        for i in range(len(arr)-2):
            for j in range(i+1,len(arr)-1):
                if abs(arr[j]-arr[i])<=a:
                    for k in range(j+1,len(arr)):
                        if abs(arr[k]-arr[j])<=b and abs(arr[i]-arr[k])<=c:
                            count+=1
                            
        return(count)

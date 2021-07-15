class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        i=0
        res = 0
        while i < len(arr)-2:
            j=i+1
            while j < len(arr)-1:
                k=j+1
                while k < len(arr):
                    if (abs(arr[i] - arr[j]) <= a) & (abs(arr[j] - arr[k]) <= b) & (abs(arr[i] - arr[k]) <= c):
                        res+=1
                    k+=1        
                j+=1
            i+=1
        return(res)

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m = arr[int((n-1)/2)]
        result = []
        l,r = 0,n-1
        count = 0
        
        while l <= r and len(result)<k:
            if abs(arr[r]-m) > abs(arr[l]-m):
                result.append(arr[r])
                r -= 1
            elif abs(arr[l]-m) > abs(arr[r]-m):
                result.append(arr[l])
                l += 1
            else:
                result.append(arr[r])
                r -= 1
        return result        
            


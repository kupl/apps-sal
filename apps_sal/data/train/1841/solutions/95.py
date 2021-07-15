class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        m = arr[(n-1)//2]
        
        res = []
        l = 0
        r = n-1
        while k > 0:
            c1 = abs(arr[l]-m)
            c2 = abs(arr[r]-m)
            
            if c1 > c2:
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r -= 1
            k -= 1
        return res

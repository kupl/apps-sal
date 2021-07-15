class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if not k or not arr:
            return []
        
        arr = sorted(arr)
        m = arr[(len(arr) - 1) // 2]
        
        l = 0
        r = len(arr) -1
        ans = []
        while k> 0 and l <= r:
            if abs(arr[l] - m) > abs(arr[r] -m):
                ans.append(arr[l])
                l += 1
            elif abs(arr[l] - m) == abs(arr[r] -m):
                if arr[l] > arr[r]:
                    ans.append(arr[l])
                    l += 1
                else:
                    ans.append(arr[r])
                    r -= 1
            else:
                ans.append(arr[r])
                r -= 1
            k -= 1
        return ans
        


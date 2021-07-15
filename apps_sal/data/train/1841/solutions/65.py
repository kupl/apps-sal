class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n= len(arr)
        if k == n:
            return arr
        
        arr.sort()
        median = arr[(n-1)//2]
        
        left, right = 0, n-1
        ans = []
        while k > 0 and left <= right:
            if abs(arr[left]-median) > abs(arr[right]-median):
                ans.append(arr[left])
                left += 1
            else:
                ans.append(arr[right])
                right -= 1
            k -= 1
                
        return ans
        


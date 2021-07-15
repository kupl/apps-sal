class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        K = len(arr)
        median = arr[(K - 1)//2]
        
        left, right = 0, len(arr) - 1
        ans = []
        print((arr, median))
        while left <= right and k > 0:
            if abs(arr[left] - median) <= abs(arr[right] - median):
                ans.append(arr[right])
                right -= 1
            else:
                ans.append(arr[left])
                left += 1    
            k -= 1
        return ans
            


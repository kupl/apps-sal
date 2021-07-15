class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        def compare(point1, point2):
            return (point1[0] ** 2 + point1[1] ** 2 - point2[0] ** 2 - point2[1] ** 2) >= 0
            
        def partition(l, r, arr):
            pivot = arr[l]
            
            while l < r:
                while l < r and compare(arr[r], pivot):
                    r -= 1
                arr[l] = arr[r]
                
                while l < r and compare(pivot, arr[l]):
                    l += 1
                arr[r] = arr[l]
            
            arr[l] = pivot
            
            return l
        
        lo = 0
        hi = len(points) - 1
        
        while lo <= hi:
            mid = partition(lo, hi, points)
            if mid == K:
                break
            if mid < K:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return points[0:K]
                
            


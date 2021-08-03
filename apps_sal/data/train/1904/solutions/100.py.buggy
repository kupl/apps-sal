class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = [(x**2 + y**2, [x,y]) for x, y in points]
        
        self.partition(dist, K, 0, len(dist) - 1)
        
        return [elem[1] for elem in dist[:min(K, len(dist))]]
    
    \"\"\"
    [035476]
    pivot = 6
    
    
    
    \"\"\"
    def partition(self, dist, K, start, end):
        if start == end:
            return
        mid = (start + end)//2
        pivot = dist[mid][0]
        left, right = start, end
    
        while left <= right:
            while left <= right and dist[left][0] < pivot:
                left += 1
            while left <= right and dist[right][0] > pivot:
                right -= 1
            if left <= right:    
                dist[left], dist[right] = dist[right], dist[left]
                left += 1
                right -= 1
            
        if right - start >= K :
            self.partition(dist, K, start, right)
        if left - start < K:
            self.partition(dist, K - (left - start), left, end)
        
        
        

class Solution:
    \"\"\"
    Sort everything and then get the first k items.
    T: O(NlogN).
    \"\"\"
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key = lambda p: p[0]**2 + p[1]**2)[:k]    
    
    \"\"\"
    Use a max-heap to store the k smallest items.
    T: O(N log K).
    \"\"\"
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x,y in points:
            # We put the -ve sign becase we want this to be a max heap.
            key = -(x**2 + y**2)
            heapq.heappush(heap, (key, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x,y] for distance, x, y in heap]
    
    \"\"\"
    Use QuickSelect.
    T: O(N) in the average case; O(N^2) in the worst case.
    \"\"\"
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quickSelect(points, k - 1, 0, len(points) - 1)
        return points[:k]
    
    def quickSelect(self, points, k, p, q):
        partitionIndex  = self.partition(points, p, q)
        if partitionIndex == k:
            return partitionIndex
        elif partitionIndex > k:
            return self.quickSelect(points, k, p, partitionIndex  - 1)
        else:
            return self.quickSelect(points, k, partitionIndex + 1, q)
                
    def getDistance(self, p):
        x,y = p 
        return x**2 + y**2
    
    # p <= k <= boundary: items that are smaller than the pivot.
    # boundary + 1 <= < q: items that are bigger than the pivot.
    def partition(self, points, p, q):
        distancePivot = self.getDistance(points[q])
        boundary = p - 1
        
        for j in range(p, q):
            if self.getDistance(points[j]) < distancePivot:
                boundary += 1
                points[boundary], points[j] = points[j], points[boundary]                
        
        # Insert the pivot in the correct position.
        boundary += 1 
        points[boundary], points[q] = points[q], points[boundary]
        
        return boundary

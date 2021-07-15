class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # nlog(n)
        # points.sort(key=lambda item: item[0]**2 + item[1]**2)
        # return points[:K]
        
        # nlog(k)
        # return heapq.nsmallest(K, points, key=lambda item: item[0]**2 + item[1]**2)
        
        # O(n)
        def compare(p1, p2):
            return p1[0]**2 + p1[1]**2 - (p2[0]**2 + p2[1]**2)
        
        def partition(points, l, r):
            pivot = points[l]
            while l < r:
                while l < r and compare(points[r], pivot) >=0:
                    r -= 1
                points[l] = points[r]
                while l < r and compare(points[l], pivot) <=0:
                    l += 1
                points[r] = points[l]
            points[l] = pivot
            return l
        
        l, r = 0, len(points) - 1
        while l < r:
            p = partition(points, l, r)
            if p == K - 1:
                break
            if p < K - 1:
                l = p + 1
            else:
                r = p - 1
        return points[:K]

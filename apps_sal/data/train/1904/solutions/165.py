# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         points.sort(key=lambda x: math.sqrt(x[0]*x[0] + x[1]*x[1]))
#         return points[:K]
    
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = lambda x: math.sqrt(points[x][0]**2 + points[x][1]**2)
        def dc(i, j, K):
            if i >= j: return
            oi, oj = i, j
            i += 1
            pivot = dist(oi)
            while True:
                while i < j and dist(i) < pivot: i += 1
                while i <= j and dist(j) >= pivot: j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]
            points[oi], points[j] = points[j], points[oi]
            if K-1 == j: return
            elif K-1 < j: dc(oi, j, K) 
            else: dc(j+1, oj, K)
        dc(0, len(points)-1, K)
        return points[:K]
            


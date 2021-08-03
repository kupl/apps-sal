class DistanceSort(List[int]):
    
    def __lt__(lhs, rhs):
        ldiff = lhs[0]*lhs[0] + lhs[1]*lhs[1]
        rdiff = rhs[0]*rhs[0] + rhs[1]*rhs[1]
        return ldiff < rdiff
    
class Solution:
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        return sorted(points, key=DistanceSort)[:K]
        
\"\"\"
\"\"\"

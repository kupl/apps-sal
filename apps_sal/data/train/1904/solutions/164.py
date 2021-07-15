# Quick select: time = O(N)
# Logic to understand https://leetcode.com/problems/k-closest-points-to-origin/discuss/220235/Java-Three-solutions-to-this-classical-K-th-problem.
# clean code https://leetcode.com/problems/k-closest-points-to-origin/discuss/219442/Python-with-quicksort-algorithm

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        self.qkSel(points, 0, len(points)-1, K)
        return points[:K]
    
    def qkSel(self, points, l, r, K):
        if l > r: return 
        
        idx = random.randint(l, r)
        points[idx], points[r] = points[r], points[idx]  
        i = l
        
        for j in range(l, r):
            if self.cmp(points[j], points[r]):
                points[i], points[j] = points[j], points[i]
                i += 1
                
        points[i], points[r] = points[r], points[i] 
        
        if i == K: return 
        elif i < K: return self.qkSel(points, i+1, r, K)
        elif i > K: return self.qkSel(points, l, i-1, K)
        
    
    def cmp(self, p1, p2):
        return (p1[0]**2 + p1[1]**2) - (p2[0]**2 + p2[1]**2) < 0  
        
                
        
        
        
        
        
        


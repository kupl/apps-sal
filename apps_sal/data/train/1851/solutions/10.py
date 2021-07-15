class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        step = 0 
        l, r = -1, 0
        for i,j in sorted(clips):
            if r >= T:
                return step
            if i>r:
                return -1
            
            if l<i<=r:
                step += 1
                l = r          
            r = max(r, j)            
        return step if r>=T else -1

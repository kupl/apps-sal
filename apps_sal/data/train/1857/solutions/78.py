class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ht = {}
        
        for i, j in reservedSeats:
            if not (i-1) in ht:
                ht[i-1] = [0] * 10
            ht[i-1][j-1] = 1
        
        ans = (n-len(ht)) * 2
        
        for i in ht:
            inc = 0
            if ht[i][1:5] == [0, 0, 0, 0]:
                inc += 1
            if ht[i][5:9] == [0, 0, 0, 0]:
                inc += 1
            if inc >= 1:
                ans += inc
                continue
            if ht[i][3:7] == [0, 0, 0, 0]:
                ans += 1
        
        return ans

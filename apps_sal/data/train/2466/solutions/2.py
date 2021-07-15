class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        leng = len(mat[0])
        ans = 0
        seen = set()
        for i in range(leng):
            ans+=mat[i][i]
            seen.add((i,i))
            
        ctr = len(mat)-1
        for i in range(leng):
            if (i,leng-1) not in seen:
                ans+=mat[i][leng-1]
            leng-=1
            
        return ans


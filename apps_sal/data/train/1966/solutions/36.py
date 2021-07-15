class Solution:
    def countOnes(self, nums):
        res = 0
        length = 0
        for i in range(len(nums)):
            length = 0 if nums[i] == 0 else length + 1
            res += length
        return res
        
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        
        n, m = len(mat), len(mat[0])
        res = 0
        
        for i in range(n):
            h = [1] * m
            
            for j in range(i, n):
                for k in range(m):
                    if mat[j][k] == 0:
                        h[k] = 0
                res += self.countOnes(h)
        
        return res
                


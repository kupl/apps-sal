class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        heights = [0] * n
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1
                   

            for j in range(n):
                k = j
                smallest_height = heights[k]
                
                while k > -1 and heights[k] > 0:
                    smallest_height = min(smallest_height, heights[k])
                    count += smallest_height
                    k -= 1

        return count

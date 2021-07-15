class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat: return 0
        
        rows, cols = len(mat), len(mat[0])
        height = [0] * cols
        output = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    height[c] = 0
                else:
                    height[c] += 1
                    v = height[c]
                    for i in range(c, -1, -1):
                        if height[i] == 0: break
                        v = min(v, height[i])
                        output += v
        return output
    
    
#     public int numSubmat(int[][] mat) {
#         int m = mat.length, n = mat[0].length, height[] = new int[n], res = 0; 
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 height[j] = mat[i][j] == 0 ? 0 : height[j] + 1;   //  height of histogram;
#                 for (int k = j, min = height[j]; k >= 0 && min > 0; k--) {
#                     min = Math.min(min, height[k]);
#                     res += min;
#                 }
#             }
#         }
#         return res;
#     }


        
        
        1 + 1 + 2 + 1 + 1 + 3 + 2+ 2
        
        


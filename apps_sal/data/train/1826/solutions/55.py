class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        
        height = len(mat)
        width = len(mat[0])
        
        z = [[None for _ in range(width)] for _ in range(height)]
        
        for x in range(width):
            for y in range(height):
                z[y][x] = sum(
                    [
                        i for j in [
                        row[max(x - K, 0): x + K + 1] for row in mat[max(y - K, 0): y + K + 1]
                        ] for i in j
                    ]
                ) 
        
        
        return z

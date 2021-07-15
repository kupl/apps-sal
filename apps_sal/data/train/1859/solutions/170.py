class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        def traverse_subsquares(i, j):
            max_size = min(i, j) + 1
            n_subsquares = 0
            for i_base in range(i, i - max_size, -1):
                size = i - i_base + 1
                ip = i_base
                for jp in range(j, j - size, -1):
                    if not matrix[ip][jp]:
                        return n_subsquares
                for ip in range(i_base + 1, i_base + size, 1):
                    if not matrix[ip][jp]:
                        return n_subsquares
                n_subsquares += 1
                
            return n_subsquares
        
        total = 0
        for i in range(rows):
            for j in range(cols):
                n = traverse_subsquares(i, j)
                total += n
                
        return total

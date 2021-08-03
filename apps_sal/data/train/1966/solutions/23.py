class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        answer = 0
        row, col = len(mat), len(mat[0])
        # Get the number of 1's to the right of the current 1
        # For example:
        # [1, 0, 1]
        # [1, 1, 0]
        # [1, 1, 0]
        # turns into
        # [1, 0, 1]
        # [2, 1, 0]
        # [2, 1, 0]
        one_counts = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            counter = 0
            for c in range(col - 1, -1, -1):
                if mat[r][c] == 1:
                    counter += 1
                    one_counts[r][c] = counter
                else:
                    counter = 0
        # Go through each element in the matrix, and if it is == 1, check how many
        # submatricies with this element as the top leftmost point can we generate
        for r in range(row):
            for c in range(col):
                if mat[r][c] == 1:
                    min_width = float('inf')
                    for k in range(r, row):
                        if mat[k][c] == 1:
                            min_width = min(min_width, one_counts[k][c])
                            answer += min_width
                            continue
                        break
        return answer

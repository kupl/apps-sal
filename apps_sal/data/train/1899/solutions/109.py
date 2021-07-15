class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        row_shifts = [-1, 0, 1, 0]
        col_shifts = [0, 1, 0, -1]
            
        def bfs_mark_first(row, col, mark):
            nonlocal A, row_shifts, col_shifts
            queue = [(row, col)]
            edges = []
            while len(queue) > 0:
                curr_row, curr_col = queue.pop(0)
                if A[curr_row][curr_col] == mark:
                    continue
                A[curr_row][curr_col] = mark
                add_to_edges = False
                for row_shift, col_shift in zip(row_shifts, col_shifts):
                    new_row = curr_row + row_shift
                    new_col = curr_col + col_shift
                    if 0 <= new_row < len(A) and 0 <= new_col < len(A[0]):
                        if A[new_row][new_col] == 1:
                            queue.append((new_row, new_col))
                        else:
                            add_to_edges = True
                if add_to_edges:
                    edges.append((curr_row, curr_col))
            return edges
        
        terminate = False
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col] == 1:
                    edges = bfs_mark_first(row, col, -1)
                    terminate = True
                    break
            if terminate:
                break
                    
        queue = edges
        # print(edges)
        while len(queue) > 0:
            curr_row, curr_col = queue.pop(0)
            for row_shift, col_shift in zip(row_shifts, col_shifts):
                new_row = curr_row + row_shift
                new_col = curr_col + col_shift
                if 0 <= new_row < len(A) and 0 <= new_col < len(A[0]):
                    if A[new_row][new_col] == 0:
                        A[new_row][new_col] = A[curr_row][curr_col] - 1
                        queue.append((new_row, new_col))
                    if A[new_row][new_col] == 1:
                        return abs(A[curr_row][curr_col]) - 1
        
        return -1

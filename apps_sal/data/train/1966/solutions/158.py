class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        h, w = len(mat), len(mat[0])
        dp_acc_of_1 = [ [ 0 for _ in range(w)] for _ in range(h) ]
        for y in range(h):
            for x in range(w):
                if x == 0:
                    dp_acc_of_1[y][x] = mat[y][x]
                else:
                    if mat[y][x] == 1:
                        dp_acc_of_1[y][x] = dp_acc_of_1[y][x-1] + 1
        counter_of_rectangle = 0
        for y in range(h):
            for x in range(w):               
                minimum_width = dp_acc_of_1[y][x]
                for h_idx in range(y, -1, -1):
                    minimum_width = min(minimum_width, dp_acc_of_1[h_idx][x])
                    counter_of_rectangle += minimum_width
                    
                    if minimum_width == 0:
                        break
        return counter_of_rectangle

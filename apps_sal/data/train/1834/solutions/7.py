class Solution(object):
    def matrixScore(self, A):
        \"\"\"
        :type A: List[List[int]]
        :rtype: int
        \"\"\"
        def flip_row(arr):
            if arr[0] == 0:
                arr = [1-arr[i] for i in range(len(arr))]
            return arr
        
        def flip_cols(arr):
            flipped_arr = [1-arr[i] for i in range(len(arr))]
            num_ones_orig = 0
            for i in range(len(arr)):
                if arr[i] == 1:
                    num_ones_orig += 1
            num_ones_flipped = 0
            for i in range(len(flipped_arr)):
                if flipped_arr[i] == 1:
                    num_ones_flipped += 1
            if num_ones_orig > num_ones_flipped:
                return arr
            return flipped_arr
                
        # flip rows
        for i in range(len(A)):
            A[i] = flip_row(A[i])
            
        # flip cols
        for j in range(1, len(A[0])):
            res_flipped = flip_cols([A[i][j] for i in range(len(A))])
            for x in range(len(A)):
                A[x][j] = res_flipped[x]
        
        sum_total = 0
        for i in range(len(A)):
            binary_number = \"\".join([str(elem) for elem in A[i]])
            int_number = int(binary_number, 2)
            sum_total += int_number
        
        return sum_total

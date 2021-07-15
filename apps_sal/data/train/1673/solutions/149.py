class Solution:
    def minFallingPathSum1(self, arr: List[List[int]]) -> int:
        '''
        Time: O(mn^2)  - due linear search for min in inner loop
        Space: O(n + n) ~ O(n)
        '''
        m = len(arr)
        n = len(arr[0])
        
        if m == 1: # 1 ele sq. matrix
            return arr[0][0]
        
        def get_min_neighbors(j):
            a, row_prev[j] = row_prev[j], float('inf')
            min_val = min(row_prev)
            row_prev[j] = a
            return min_val
        
        row_prev = arr[0]
        cur = [0]*n
        global_min = float('inf')
        
        for row in range(1, m):
            for col in range(n):
                cur[col] = get_min_neighbors(col) + arr[row][col]
                
                if row == m-1 and cur[col] < global_min:
                    global_min = cur[col]
     
            row_prev = cur[:]
        
        return global_min

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        '''
        Time: O(mn) - if heapq.nsmallest is linear, here min search is in outer loop
        Space: O(n + n) ~ O(n)
        '''
        m = len(arr)
        n = len(arr[0])
        
        if m == 1: # 1 ele sq. matrix
            return arr[0][0]
        
        def get_min_neighbors():
            min1, min2 = heapq.nsmallest(2, row_prev)
            return min1, min2
        
        row_prev = arr[0]
        cur = [0]*n
        global_min = float('inf')
        
        for row in range(1, m):
            min1, min2 = get_min_neighbors() #if linear
            for col in range(n):
                min_val = min1 if row_prev[col] != min1 else min2 #doesnt matter if duplicates
                cur[col] = min_val + arr[row][col] 
                
                if row == m-1 and cur[col] < global_min:
                    global_min = cur[col]
     
            row_prev = cur[:]

        return global_min

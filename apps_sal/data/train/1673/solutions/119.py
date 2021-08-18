'''
find the minimum of the previous row and add it to the minimum of the current row if they are not in the same column

else -> add the second smallest from the previous to the min in current row

'''
import heapq


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows, cols = len(arr), len(arr[0])
        for i in range(1, rows):
            min1, min2 = heapq.nsmallest(2, arr[i - 1])
            '''min1 = min(arr[i-1])
            min1_index = arr[i-1].index(min1)
           
            min2 = min(x for j,x in enumerate(arr[i-1]) if j!=min1_index )'''
            for j in range(cols):
                if arr[i - 1][j] == min1:
                    arr[i][j] += min2
                else:
                    arr[i][j] += min1
        return min(arr[-1])

import heapq
import numpy as np


class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        x = len(arr)
        new_count = np.zeros((x, x))
        new_count[0] = arr[0]
        for k in range(1, x):
            previous_line_maxes = heapq.nsmallest(2, new_count[k - 1])
            for index in range(len(arr)):
                if new_count[k - 1][index] == previous_line_maxes[0]:
                    value_to_add = previous_line_maxes[1]
                else:
                    value_to_add = previous_line_maxes[0]
                new_count[k, index] = value_to_add + arr[k][index]
        return int(min(new_count[-1]))

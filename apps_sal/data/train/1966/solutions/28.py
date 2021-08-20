import copy
from math import sqrt
from typing import List
import numpy
import sys


class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        height = [0] * col
        result = 0
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    height[j] = 0
                else:
                    height[j] = height[j] + 1
                k = j
                minvalue = sys.maxsize
                while k >= 0 and height[k] != 0:
                    minvalue = min(minvalue, height[k])
                    result += minvalue
                    k -= 1
                pass
            pass
        return result

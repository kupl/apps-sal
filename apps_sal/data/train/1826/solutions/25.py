import numpy as np
import scipy.signal
#convolve2d as convolv

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        mat = np.array(mat)
        return scipy.signal.convolve2d(mat, np.ones((2*K +1, 2*K + 1)), mode=\"same\").astype('int')
        

from scipy import signal
import numpy as np


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        N = 2 * K + 1
        return signal.convolve2d(mat, np.ones((N, N)), mode='same').astype(int)

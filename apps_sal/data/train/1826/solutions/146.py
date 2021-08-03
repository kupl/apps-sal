class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        import numpy as np
        from scipy.signal import convolve2d
        mat = np.array(mat, dtype=int)
        convolution = np.ones((2 * K + 1, 2 * K + 1), dtype=int)
        mat = convolve2d(mat, convolution, 'same')
        return mat

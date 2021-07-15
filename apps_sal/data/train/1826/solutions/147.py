class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        from numpy import array, ones
        from scipy.signal import convolve2d
        
        mat = array(mat, dtype = int)
        convolution = ones((2 * K + 1, 2 * K + 1), dtype = int)
        mat = convolve2d(mat, convolution, 'same')
        
        return mat

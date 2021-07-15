\"\"\"
google onsite 
二维矩阵包含0和1。问由0组成的sub rectangle有多少个，这个是面经题

我是这样想的不知道对不对，考虑以(i, j)为右下角的最大正方形边长，这个就是lc 221。然后如果以(i, j)为右下角的最大正方形边长是a，则以它为右下角的正方形数目是a，所以把这些加起来就好
因此用以下 dp方法

dp[i][j] 以(i, j)为右下顶点的最大全1矩阵的边长. 也表示 以（i,j）为右下角正方形数量
答案为 sum(dp[i][j])
\"\"\"

\"\"\"
Google onsite
给一个由0，1组成的数组，算子数组全是0的个数。 e.g.[0,0,1,0] 返回4
follow up: 输入是二维矩阵，算子矩阵全是0的个数
\"\"\"

\"\"\"

固定上下边界，找到以当前长度为矩形高的 矩形数量，最后得到总数量

fix up boundary and bottom boundary then find all submatrix with this height 
for how to get all submatrix with this height, we build a array, idx is col idex, val is 1 if all the cells between up and bottom are one, otherwise zero 
than we convert this 2d problem to 1d, we just need to calculate how many rec with all ones in it in this array 

Note: the array h[k] == 1 means all values in column k from row \"up\" to \"down\" are 1 (that's why we use &). So overall, the idea is to \"compress\" the 2D array to the 1D array, and apply 1D array method on it, while trying all heights up to down.


Time O(M * N * M)
Space O(M * N )
\"\"\"
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0 
        n = len(mat)
        m = len(mat[0])
        count = 0
        # enumerate top and bottom boundary  
        for top in range(n):
            arr = [1] * m
            for bottom in range(top, n):
                # convert 2d to 1d array 
                for col in range(m):
                    arr[col] &= mat[bottom][col]
                # get all count of submatrices whose height = bottome - top
                count += self.get_arr_ones_count(arr)
        return count 
    # use curr num as the right boundary of the rectangle 
    def get_arr_ones_count(self, arr):
        res = 0
        count = 0
        for num in arr:
            if num == 0:
                count = 0
            else:
                count += 1 
                res += count 
        return res 
# [[1,0,1],
#  [1,1,0],
#  [1,1,0]]
# arr = [1,0,1], top=0,bottom=0, count = 2
# arr = [2,1,1], top=0,bottom=1, count = 2



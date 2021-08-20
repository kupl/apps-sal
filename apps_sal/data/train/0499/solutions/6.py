"""
            [1,2,3,2,1]

diff array: [1,1,1,-1,-1]

presum: [1,3,6,8,9]

差分数组：a[i] - a[i-1]


对数组A[i:j]区间每个数都加k -> diff[i] + k,   diff[j] - k （j之后的数并不想+k, 所以要减回去）  -> 这样就能还原出一个符合要求的数组了
对[1,2,3,2,1] 区间[1:4] 每个元素都+1 ： 
diff [1,2,1,-1,-2]
还原数组 [1,3,4,3,1]


target = [1,2,3,2,1] -> 求diff -> [1,1,1,-1,-1]

若此题转化为求diff数组
[0,0,0,0,0] -> [1,1,1,-1,-1]

因为每次在一个区间连续+1 相当于在这个区间的第一个diff元素加一，结尾后面一个diff元素-1，此题中-1可选 因为我们最多可以把这个区间扩大到n， 所以 求diff里面positive数的和 就是答案



"""


class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        diff = [0] * len(target)
        diff[0] = target[0]
        for (i, num) in enumerate(target[1:], 1):
            diff[i] = target[i] - target[i - 1]
        opr = 0
        for d in diff:
            if d > 0:
                opr += d
        return opr

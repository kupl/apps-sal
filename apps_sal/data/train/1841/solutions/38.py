from collections import defaultdict


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        # Method 1
        # 计算median
        # 挨个计算绝对值，保存(key:abs,value:[num])
        # key[从大到小]，value从大到小。res到达k的长度，就return

        # Method 2
        # 计算median
        # 在排过序的list中，找到最左和最右 对比他们的abs（x-median）
        # 如果abs一样，则比较他们的原本大小。
        # 不然大的那个丢进去，大的指针前进，小的指针留在原位
        # 直到k = 0

        arr = sorted(arr)
        n = len(arr)
        median = arr[(n - 1) // 2]

        l, r = 0, n - 1
        res = []

        for i in range(k):
            if abs(arr[l] - median) > abs(arr[r] - median):
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r -= 1

        return res


#         n = len(arr)
#         new_a = sorted(arr)
#         median = new_a[(n-1)//2]
#         d = defaultdict(list)

#         for x in arr:
#             d[abs(x-median)].append(x)

#         d = sorted(d.items(), key = lambda x: x[0],reverse = 1)
#         res = []
#         for x in d:
#             if len(x[1]) <= k:
#                 res += x[1]
#                 k -= len(x[1])
#             else:
#                 tar = sorted(x[1])[::-1]
#                 i = 0
#                 while k > 0:
#                     res.append(tar[i])
#                     k-=1
#                     i += 1
#                 return res
#         return res

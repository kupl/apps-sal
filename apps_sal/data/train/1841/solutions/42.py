from collections import defaultdict
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        # 计算median
        # 挨个计算绝对值，保存(key:abs,value:[num])
        # key[从大到小]，value从大到小。res到达k的长度，就return
        
        n = len(arr)
        new_a = sorted(arr)
        median = new_a[(n-1)//2]
        d = defaultdict(list)
        
        for x in arr:
            d[abs(x-median)].append(x)
        
        d = sorted(d.items(), key = lambda x: x[0],reverse = 1)
        res = []
        for x in d:
            if len(x[1]) <= k:
                res += x[1]
                k -= len(x[1])
            else:
                tar = sorted(x[1])[::-1]
                i = 0
                while k > 0:
                    res.append(tar[i])
                    k-=1
                    i += 1
                return res
        return res

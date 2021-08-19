import collections


class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dic = {}
        lst = [0] * len(barcodes)
        for i in barcodes:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        sorted_x = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
        sorted_dict = collections.OrderedDict(sorted_x)
        var = 0
        for (i, j) in sorted_dict.items():
            for _ in range(j):
                lst[var] = i
                var += 2
                if var >= len(barcodes):
                    var = 1
        return lst

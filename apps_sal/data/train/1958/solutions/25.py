class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        dic = {}
        for (idx, size) in enumerate(groupSizes):
            if size == 1:
                res.append([idx])
            elif size > 1:
                if size not in dic:
                    dic[size] = [idx]
                else:
                    dic[size].append(idx)
                    if len(dic[size]) == size:
                        res.append(dic[size])
                        del dic[size]
        return res

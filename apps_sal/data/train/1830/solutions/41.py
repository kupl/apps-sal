from sortedcontainers import SortedList


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [1 for i in range(len(rains))]
        ls, zs = {}, SortedList()
        for i, l in enumerate(rains):
            if l in ls:
                if len(zs) == 0:
                    return []
                else:
                    p = zs.bisect(ls[l])
                    if p == len(zs):
                        return []
                    res[zs[p]] = l
                    zs.pop(p)
                    res[i] = -1
                    ls[l] = i
            elif l != 0:
                ls[l] = i
                res[i] = -1
            else:
                zs.add(i)
        return res

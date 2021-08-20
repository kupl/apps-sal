import numpy as np


class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        c = set(groupSizes)
        cn = []
        for i in c:
            newlist = [j for (j, val) in enumerate(groupSizes) if val == i]
            if len(newlist) > i:
                newlist = [newlist[j:j + i] for j in range(0, len(newlist), i)]
                cn.extend(newlist)
            else:
                cn.append(newlist)
        return cn

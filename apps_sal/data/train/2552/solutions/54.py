import numpy as np


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # temp=np.unique(arr)
        # le = len(arr)
        # for i in temp:
        #     if (arr.count(i)/le>0.25):
        #         return i
        return collections.Counter(arr).most_common(1)[0][0]
        # print(collections.Counter(arr).most_common(1))

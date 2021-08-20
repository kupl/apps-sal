import collections


class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        dic = Counter(A)
        for i in dic:
            if dic[i] > 1:
                return i

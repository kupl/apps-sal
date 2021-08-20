class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        dic = {}
        for i in A:
            if i not in dic:
                dic[i] = 0
            else:
                return i

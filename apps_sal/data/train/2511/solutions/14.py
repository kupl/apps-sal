class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        dic = {}
        for element in A:
            if not element in dic:
                dic[element] = 1
            else:
                return element

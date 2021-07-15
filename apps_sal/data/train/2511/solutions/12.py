class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic = collections.Counter(A)
        for num in dic:
            if dic[num] > 1:
                return num

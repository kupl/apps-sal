class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count_dict = collections.Counter(A)
        for key, value in list(count_dict.items()):
            if value > 1:
                return key
            


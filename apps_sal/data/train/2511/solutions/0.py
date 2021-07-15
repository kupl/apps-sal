class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dict_ = dict()
        
        for a in A:
            if a in dict_:
                return a
            else:
                dict_[a] = 1


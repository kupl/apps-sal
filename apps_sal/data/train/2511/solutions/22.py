class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = collections.Counter(A)
        mostc = counter.most_common(1)
        
        for key,value in mostc:
            return key

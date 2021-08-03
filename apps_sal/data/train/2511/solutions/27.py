class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = collections.Counter(A)

        for i in count:
            if count[i] > 1:
                return i

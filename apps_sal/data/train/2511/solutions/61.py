class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = collections.Counter(A)
        repeat = len(A) // 2
        for key in count:
            if count[key] == repeat:
                return key
        return -1

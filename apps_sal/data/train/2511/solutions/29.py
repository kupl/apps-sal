class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        record = set()
        for a in A:
            if a in record:
                return a
            else:
                record.add(a)

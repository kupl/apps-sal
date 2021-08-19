from collections import Counter


class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        counter = Counter(A)
        return counter.most_common(1)[0][0]

from collections import Counter as C


class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        s = C(A).most_common()
        return s[0][0]

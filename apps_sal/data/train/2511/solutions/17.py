from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        cnt = Counter(A).most_common(1)
        return cnt[0][0]

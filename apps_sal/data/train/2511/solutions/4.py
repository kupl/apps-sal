from collections import Counter as di


class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        d = di(a)
        maxi = (len(a) // 2)
        return d.most_common(1)[0][0]
        for i in d:
            if d[i] == maxi:
                return i

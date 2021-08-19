from collections import Counter


class Solution:

    def repeatedNTimes(self, A: List[int]) -> int:
        ans = 0
        c = Counter(A)
        count = 0
        for i in c:
            print('{} = {}'.format(i, c[i]))
            if c[i] > count:
                count = c[i]
                ans = i
        return ans

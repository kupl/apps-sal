import collections


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        lst = collections.defaultdict(list)

        for r, c in reservedSeats:
            lst[r].append(c)
        ret = n * 2
        for r in lst:
            flag1 = False
            flag2 = False
            flag3 = False
            for c in lst[r]:
                if 2 <= c <= 5:
                    flag1 = True
                if 6 <= c <= 9:
                    flag2 = True
                if 4 <= c <= 7:
                    flag3 = True
            if flag1:
                ret -= 1
            if flag2:
                ret -= 1
            if (flag1 and flag2) and not flag3:
                ret += 1
        return ret

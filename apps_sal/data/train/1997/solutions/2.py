class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        from functools import cmp_to_key

        def cmp(a, b):
            if a[0] > b[0]:
                return 1
            if a[0] < b[0]:
                return -1
            if a[1] > b[1]:
                return -1
            return 1

        lis = []
        if len(intervals) == 1:
            return 1
        for x, y in intervals:
            lis.append((x, y))
        lis.sort(key=cmp_to_key(cmp))
        fin = []
        fin.append(list(lis[0]))
        for i in range(1, len(lis)):
            currx, curry = lis[i]
            flag = 0
            for j in range(len(fin)):
                if curry <= fin[j][1] and currx >= fin[j][0]:
                    flag = 1
            if flag == 0:
                fin.append([currx, curry])
        return len(fin)

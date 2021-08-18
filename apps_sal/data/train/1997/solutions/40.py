class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        lis = intervals
        arr = []
        lis.sort()
        for i in range(0, len(lis)):
            if lis[i] in arr:
                continue
            for j in range(i + 1, len(lis)):
                if i < len(lis) and j < len(lis):
                    if (lis[i][0] >= lis[j][0] and lis[i][1] <= lis[j][1] and lis[i] not in arr):
                        arr.append(lis[i])
                    if (lis[i][0] <= lis[j][0] and lis[i][1] >= lis[j][1] and lis[j] not in arr):
                        arr.append(lis[j])
                else:
                    break
        return len(lis) - len(arr)

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        lis = intervals
        # print(\".\")
        # i = 0
        arr = []
        # print(lis)
        lis.sort()
        # print(lis)
        # count = 0
        for i in range(0, len(lis)):
            # temp = lis.copy()
            # print(lis)
            if lis[i] in arr:
                continue
            for j in range(i + 1, len(lis)):
                if i < len(lis) and j < len(lis):
                    # print(\".\")
                    if (lis[i][0] >= lis[j][0] and lis[i][1] <= lis[j][1] and lis[i] not in arr):
                        # print(\"if\",lis[i],lis[j])
                        arr.append(lis[i])
                        # lis.remove(lis[i])
                    if (lis[i][0] <= lis[j][0] and lis[i][1] >= lis[j][1] and lis[j] not in arr):
                        # print(\"elif \",lis[j],lis[i])
                        arr.append(lis[j])
                        # lis.remove(lis[j])
                    # else:
                        # i = i + 1
                else:
                    break
            # lis = temp.copy()
        return len(lis) - len(arr)
#         Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2

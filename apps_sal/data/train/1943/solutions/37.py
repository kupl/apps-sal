class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []
        MergedList = A + B
        MergedList.sort()
        result = []
        for i in range(len(MergedList)):
            if i == 0:
                continue
            if MergedList[i][0] <= MergedList[i - 1][1]:
                result.append([max(MergedList[i - 1][0], MergedList[i][0]), min(MergedList[i - 1][1], MergedList[i][1])])
                MergedList[i][1] = max(MergedList[i - 1][1], MergedList[i][1])
        
        return result


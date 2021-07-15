class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if len(arr) ==1:
            return arr[0][0]
        else:
            Row = len(arr)
            Col = len(arr[0])
            ResultMat = [arr[0]] 
            for i in range(1,Row):
                ResultList = []
                for j in range(Col):
                    NewList= ResultMat[i-1]
                    NewList = NewList[0:j] + NewList[(j+1):len(NewList)]
                    Min = min(NewList)
                    Value = Min+arr[i][j]
                    ResultList.append(Value)
                ResultMat.append(ResultList)
            return min(ResultMat[Row-1])

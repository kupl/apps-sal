class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        nR = len(mat)
        nC = len(mat[0])
        newMat = [[None for j in range(nC)] for i in range(nR)]
        for r,row in enumerate(mat):
            i = 0
            while i<nC:
                if i-K>=0:
                    newMat[r][i] = sum(row[(i-K):(i+K+1)])
                    i+=1
                else:
                    newMat[r][i] = sum(row[0:(i+K+1)])
                    i+=1
        
        finalAns = [[0 for j in range(nC)] for i in range(nR)]
        
        rowNum = 0
        while rowNum<nR:
            print(\"This is rowNum:\",rowNum)
            if rowNum-K<=0:
                minRow = 0
            else:
                minRow = rowNum-K

            if rowNum+K>=nR:
                maxRow = nR
            else:
                maxRow = rowNum+K+1
                
            print(minRow,maxRow)    
            for col in range(nC):
                for r in range(minRow,maxRow):
                    finalAns[rowNum][col] += newMat[r][col]
            rowNum+=1
        
        return finalAns

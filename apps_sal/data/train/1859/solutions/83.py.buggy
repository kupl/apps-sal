class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        
        nrows = len(matrix)
        ncols = len(matrix[0])
        mainDict = {\"numBelow\":0,\"numRight\":0}
        test = [[None for i in range(ncols)] for j in range(nrows)]
        for r in reversed(range(nrows)):
            for c in reversed(range(ncols)):
                if r == nrows-1 and c== ncols-1:
                    if matrix[r][c]:
                        temp = {\"numBelow\":1,\"numRight\":1}
                        test[r][c] = temp
                    else:
                        test[r][c] = mainDict
                    continue
                elif r == nrows-1:
                    if matrix[r][c]:
                        numRight = test[r][c+1][\"numRight\"]+1
                        temp = {\"numBelow\":1,\"numRight\":numRight}
                        test[r][c] = temp
                    else:
                        test[r][c] = mainDict
                    continue
                elif c == ncols-1:
                    if matrix[r][c]:
                        numBelow = test[r+1][c][\"numBelow\"]+1
                        temp = {\"numBelow\":numBelow,\"numRight\":1}
                        test[r][c] = temp
                    else:
                        test[r][c] = mainDict
                else:
                    if matrix[r][c]:
                        currNumRight = test[r][c+1][\"numRight\"]+1
                        numBelow = test[r+1][c][\"numBelow\"]+1
                        temp = {\"numBelow\":numBelow,\"numRight\":currNumRight}
                        test[r][c] = temp
                    else:
                        test[r][c] = mainDict
        
        count = 0
        for r in range(nrows):
            for c in range(ncols):
                if matrix[r][c]:
                    print(r,c)
                    numRight = test[r][c][\"numRight\"]
                    numBelow = test[r][c][\"numBelow\"]
                    minCount = min(numRight,numBelow)
                    
                    temp = 0
                    for i in reversed(range(minCount)):
                        check = True
                        for j in range(i+1):
                            if test[r+j][c][\"numRight\"]>=(i+1):
                                continue
                            else:
                                check = False
                                break
                        if check:
                            break
                    if (i+1)>1:
                        count+=(i+1)
                    else:
                        count+=1
                    
                    
        return count                
#[
# [0,1,1,1],
# [1,1,0,1],
# [1,1,1,1],
# [1,0,1,0]]

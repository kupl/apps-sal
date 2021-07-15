class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if(mat[i][j]==1):
                    #print('pos 0: ',i, ', ', j)
                    count += 1
                    down = 0
                    right = 0
                    for x in range(i+1,len(mat)):
                        if(mat[x][j]!=1):
                            break
                        #print(x, ', ',j)
                        count += 1
                        down += 1
                    for x in range(j+1,len(mat[i])):
                        if(mat[i][x]!=1):
                            break
                        #print(i,', ',x)
                        count += 1
                        right += 1
                    if(down>0 and right>0):
                        for x in range(1,down+1):
                            for y in range(1,right+1):
                                if(mat[i+x][j+y]!=1):
                                    right = y-1
                                    break
                                #print(i+x,', ',j+y)
                                count += 1
        return(count)


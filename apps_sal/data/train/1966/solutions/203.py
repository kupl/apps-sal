class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        dph = [[0 for j in range(len(mat[0])+1)] for i in range(len(mat)+1)]
        dpv = [[0 for j in range(len(mat[0])+1)] for i in range(len(mat)+1)]
        dps = [[[] for j in range(len(mat[0])+1)] for i in range(len(mat)+1)]
        
        counts = 0
        for i in range(1,len(mat)+1):
            for j in range(1,len(mat[0])+1):
                if mat[i-1][j-1]==1:
                    dpv[i][j] = dpv[i-1][j]+1
                    dph[i][j] = dph[i][j-1]+1
                    
                    if dpv[i][j]-1>dpv[i-1][j-1]:
                        tmp = collections.deque([dph[i][j]])
                        for k in range(dpv[i][j]-1):
                            if k<dpv[i-1][j-1]:
                                tmp.append(min(dps[i-1][j-1][k]+1,dph[i][j]))
                            else:
                                tmp.append(1)
                    else:
                        tmp = collections.deque([dph[i][j]])
                        for k in range(dpv[i][j]-1):
                            tmp.append(min(dps[i-1][j-1][k]+1,dph[i][j]))
                    dps[i][j] = tmp
                    counts += sum(tmp)
                    
                    
        print(dps)
        return counts

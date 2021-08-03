class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        def getmin(row):
            m1=float(\"inf\")
            indx1=0
            m2=float(\"inf\")
            indx2=0
            for elem in range(len(row)):
                #print(m1,m2)
                if row[elem]<=m1:
                    m2=m1
                    m1=row[elem]
                    indx2=indx1
                    indx1=elem
                elif row[elem]<m2:
                    m2=row[elem]
                    indx2=elem
            return indx1,indx2
        
        for i in range(1,len(arr)):
            col1,col2=getmin(arr[i-1])
            #print(col1,col2)
            for j in range(len(arr[0])):
                if j==col1:
                    arr[i][j]+=arr[i-1][col2]
                else:
                    arr[i][j]+=arr[i-1][col1]
        #print(arr)
        return min(arr[-1])

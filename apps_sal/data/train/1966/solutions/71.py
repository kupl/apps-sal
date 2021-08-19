class Solution:
    def countSubMat(self, rowmat: List[int]) -> int:
        count = rowmat[0]
        for i in range(1, len(rowmat)):
            rowmat[i] = 0 if rowmat[i] == 0 else (rowmat[i - 1] + rowmat[i])
            count += rowmat[i]

        # length=0
        # count=0
        # for i in range(len(rowmat)):
        #     length=0 if rowmat[i]==0 else (length+1)
        #     count+=length
        return count

    def numSubmat(self, mat: List[List[int]]) -> int:
        count = 0

        for m in range(len(mat)):

            h = [1 for _ in range(len(mat[0]))]
            for down in range(m, len(mat), 1):
                for n in range(len(mat[0])):
                    h[n] = h[n] and mat[down][n]

                count += self.countSubMat(h)

        return count

        # [[1,0,1],[1,1,0],[1,1,0]]
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         count=0

#         #filter size
#         for i in range(len(mat)):
#             for j in range(len(mat[0])):

#                 #for all position
#                 for a in range(len(mat)):
#                     if a+i<len(mat):
#                         for b in range(len(mat[0])):
#                             if b+j<len(mat[0]):
#                                 tmp=0

#                                 #for position inside filter
#                                 for c in range(a,a+i+1,1):
#                                     for d in range(b,b+j+1,1):
#                                         tmp+=mat[c][d]

#                                 if tmp==((i+1)*(j+1)):
#                                     count+=1
#         return count
#            #[[1,0,1],[1,1,0],[1,1,0]]

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        lx=[arr[0]]
        for i in range(1,len(arr)):
            lx.append(lx[i-1]^arr[i])
        return([lx[i[1]] if i[0]==0 else (lx[i[0]-1]^lx[i[1]]) for i in queries])
    
    
#         for i in queries:
#             if i[0]==0:
#                 ls.append(lx[i[1]])
#             else:
#                 ls.append(lx[i[0]-1]^lx[i[1]])
                
        # return ls


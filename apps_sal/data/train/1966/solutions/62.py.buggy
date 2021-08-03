class Solution:   
    def numSubmat(self, mat: List[List[int]]) -> int:    
        M=len(mat)
        N=len(mat[0])
        histogram=[[0 for _ in range(N)] for _ in range(M)] 
        dp=[[0 for _ in range(N)] for _ in range(M)] 
        ## monoI stack (index) for storing histogram 
        stack=[[] for _ in range(N)] 
        
        for m in range(M):
            for n in range(N):
                if n==0:
                    histogram[m][n]=mat[m][n]
                else:
                    histogram[m][n]=histogram[m][n-1]+1 if mat[m][n]==1 else 0
        
        res=0  
        for bottom in range(M):
            for right in range(N):
                while stack[right] and histogram[stack[right][-1]][right]>histogram[bottom][right]:
                    stack[right].pop()
                if stack[right]:
                    dp[bottom][right]=dp[stack[right][-1]][right]\\
                                        +histogram[bottom][right]*(bottom-stack[right][-1])       
                else:
                    dp[bottom][right]=histogram[bottom][right]*(bottom+1)
                    
                stack[right].append(bottom)
                res+=dp[bottom][right]  
                
        return res

    
#-----------|||||||||||||||||||||||||||||||||||||||||||||||||-------------------#   

#     ## O(M*N*M)
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         M=len(mat)
#         N=len(mat[0])
        
#         # num of consecutive ones to the left of (x,y) in the same row
#         histogram=[[0 for _ in range(N)] for _ in range(M)] 

#         for m in range(M):
#             for n in range(N):
#                 if n==0:
#                     histogram[m][n]=mat[m][n]
#                 else:
#                     histogram[m][n]=histogram[m][n-1]+1 if mat[m][n]==1 else 0
#         res=0          
#         for bottom in range(M):
#             for right in range(N):
#                 Min=histogram[bottom][right]
#                 for upper in range(bottom+1)[::-1]:      
#                     Min=min(Min,histogram[upper][right])
#                     if Min==0:
#                         break
#                     res+=Min
                    
#         return res

#-----------|||||||||||||||||||||||||||||||||||||||||||||||||-------------------#                    
        
#     ## Brute Force w/ Pruning O(N^2*M^2)
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         M=len(mat)
#         N=len(mat[0])
#         res=0       
        
#         for top in range(M):
#             for left in range(N):
#                 bound=N ## to bound the right pointer
#                 for bottom in range(top,M):                    
#                     right=left
#                     while right<bound:
#                         if mat[bottom][right]==1:
#                             res+=1
#                             right+=1
#                         else:
#                             bound=right
#                             break
#         return res                  
                        
                        
                    
                
        

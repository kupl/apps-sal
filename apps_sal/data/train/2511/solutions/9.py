from collections import Counter
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        ans = 0
        c = Counter(A)
        count = 0
        # print(c)
        for i in c:
            print(('{} = {}'.format(i,c[i])))
            if c[i]>count:
                count = c[i]
                ans = i
        return ans
    
        
        
        
        
        # dic = {}
#         ans = 0
#         for x in range(0,len(A),1):
#             if A[x] in dic:
#                 dic[A[x]] += 1
                
#                 if dic[A[x]] >ans:
#                     ans = A[x]
#             else:
#                 dic[A[x]]=1
        
        
#         return ans
                


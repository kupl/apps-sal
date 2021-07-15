import numpy as np
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        result = 0
        temp =np.zeros(60)
        for i in range(0,len(time)):
            r = time[i] % 60
            c = 60 - r
            if(temp[c % 60]>0):
                result = result +temp[c%60]
            temp[r] = temp[r] + 1
        return int(result)

                
        
#         result = 0
#         for i in range(0,len(time)-1):
#             for j in range(i+1,len(time)):
#                 if((time[i]+time[j]) % 60 ==0):
                    
#                     result = result+1
#         return result



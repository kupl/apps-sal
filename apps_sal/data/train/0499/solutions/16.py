'''
Using minimum and maximum value tracking
'''
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        tLen = len(target)
        maxValInd = [target[0], 0]
        minValInd = [target[0], 0]
        steps = target[0]
        
        for i in range(1,tLen):
            if target[i] >= maxValInd[0]:
                if not (maxValInd[1] <= minValInd[1] <= i-1):
                    steps += target[i] - maxValInd[0]
                    maxValInd = [target[i], i]
                    if target[i] <= minValInd[0]:
                        minValInd = [target[i], i]
                    
                else:
                    steps += target[i] - minValInd[0]
                    maxValInd = [target[i], i]
                    minValInd = [target[i], i]
            
            else:
                maxValInd = [target[i], i]
                if target[i] <= minValInd[0]:
                    minValInd = [target[i], i]
        
        return steps

from collections import OrderedDict 

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        numHash = {}
        for n in hand:
            if n not in numHash:
                numHash[n] = 1
            else:
                numHash[n] += 1
                
        while numHash:
            num = min(numHash)
            for n in range(W):
                nextNum = num + n
                
                if nextNum in numHash:
                    numHash[nextNum] -= 1
                    if numHash[nextNum] == 0:
                        del numHash[nextNum]
                else:
                    return False
        return True
        
        


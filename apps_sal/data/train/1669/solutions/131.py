## time - O(MlogM + M), space - O(M)
from collections import Counter, deque
class Solution:
    def isNStraightHand(self, hand, W):
        cnts = Counter(hand)
        for num in sorted(cnts):
        
            tmp = cnts[num]
            if tmp > 0:
                for j in range(num, num+W):
                    cnts[j] -= tmp
                    if cnts[j] < 0:
                        return False
        return True
 #for example, hand = [1,2,3,6,2,3,4,7,8], W = 3
#cnts: {1:1,2:2,3:2,4:1,6:1,7:1,8:1}
#=>{1:0,2:1,3:1,4:1,6:1,7:1,8:1}
#=>{1:0,2:0,3:0,4:0,6:1,7:1,8:1}
#=>{1:0,2:0,3:0,4:0,6:0,7:0,8:0}


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
        count = Counter(hand)
        
        while (count):
            init = min(count.keys())
            if count[init] ==1: 
                del count[init]
            else:
                count[init]= count[init]-1
            for i in range(1, W):

                v = count[init+1]
                if (init+1) in count.keys():
                    
                    if v==1: 
                        del count[init+1]
                    else:
                        count[init+1]= v-1
                else:
                    return False
                init = init+1
        return True

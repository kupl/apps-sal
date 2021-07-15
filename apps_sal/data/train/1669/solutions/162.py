class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand)%W!=0:
            return False
        
        hand=sorted(hand)
        dct={}
        for x in hand:
            if x not in dct:
                dct[x]=1
            else:
                dct[x]+=1
                
        '''
        below is O(N^2)? so TOO SLOW
        see https://leetcode.com/problems/hand-of-straights/discuss/135598/C%2B%2BJavaPython-O(MlogM)-Complexity
        for O(NlogN) soln
        '''        
        while len(hand)>0:
            group=[hand[0]]
            check=hand[0]
            hand.remove(check)
            while len(group)<W:
                if check+1 not in dct or dct[check+1]<1:
                    return False
                group.append(check+1)
                hand.remove(check+1)
                dct[check+1]-=1
                check+=1
        return True

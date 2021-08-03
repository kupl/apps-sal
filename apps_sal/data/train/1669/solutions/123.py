class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # Edge case: len(hand)%W!=0 that means it's not possible to split into W sized groups.
        # we can try to arrange them in form of HashMap,
        # 1:1, 2:2, 3:3, 4:4
        # if we sort them and try to find the counts, if count[i-1]>count[i] then FALSE
        # [1,2,3,6,2,3,4,7,8]
        # {1:1, 2:2, 3:2, 4:1, 6:1,7:1,8:1}
        if len(hand) % W != 0:
            return False
        else:
            while(hand != []):
                minele = min(hand)
                for i in range(0, W):
                    try:
                        hand.remove(minele + i)
                    except:
                        return False
            return True

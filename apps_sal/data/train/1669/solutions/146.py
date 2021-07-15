class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        
        #use dictionary to do quick look-up
        dic = {}
        
        for num in hand:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        hand.sort()
        
        while len(hand) > 0:
            smallest = hand[0]
            dic[smallest] -= 1
            for i in range(1,W):
                check = smallest + i
                if check not in dic:
                    return False
                else:
                    if dic[check] <= 0:
                        return False
                    else:
                        dic[check] -= 1
                        hand.remove(check)
            hand.remove(smallest)
            
        return True
            
            


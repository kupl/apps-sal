class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if not hand:
            return False
        if len(hand) % W != 0:
            return False
  
        hand.sort()
        n = len(hand)
        dic = Counter(hand)
        cards = list(dic.keys())
        cards.sort()
  
  
        for c in cards:
            num = dic[c]
            if num == 0:
                continue
            for i in range(1, W):
                if (c + i) in dic and dic[c+i] >= num:
                    dic[c+i] -= num
                else:
                    return False
  
        return True

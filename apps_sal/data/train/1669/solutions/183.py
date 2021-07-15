class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
        d = {}
        for i in hand:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        sd = {k: v for k, v in sorted(list(d.items()), key=lambda item: item[0])}
        
        while sd:
            keys = list(sd.keys())
            i = keys[0]
            sd[i] -= 1
            if sd[i] == 0: del sd[i]
            count = 1
            while count < W:
                if (i+count) not in sd:
                    return False
                else:
                    sd[i+count] -= 1
                    if sd[i+count] == 0: del sd[i+count]
                count += 1
        return True


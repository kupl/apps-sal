class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        maps = Counter(hand)
        while maps:
            k = min(maps.keys())
            count = maps[k]
            for i in range(k, k + W): 
                if i not in maps or maps[i] < count:
                    return False
                maps[i] -= count
                if maps[i] == 0:
                    maps.pop(i)
                    
        return True


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand)%W: return False
        if W==1: return True
        counts=collections.Counter(hand)
        for num in sorted(hand):
            if not counts[num]: continue
            for next in range(num,num+W):
                if next not in counts or not counts[next]: return False
                counts[next]-=1
        return True

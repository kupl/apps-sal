class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        l = len(hand)
        if l % W != 0:
            return False
        cards = Counter(hand)
        keys = sorted(list(cards.keys()))
        start = keys[0]
        start_idx = 0
        for _ in range(l//W):
            cards[start] -= 1
            for i in range(start+1, start+W):
                if i not in keys or cards[i] == 0:
                    return False
                else:
                    cards[i] -= 1
            while cards[start] == 0 and start_idx < len(keys)-1:
                start_idx += 1
                start = keys[start_idx]
        return True

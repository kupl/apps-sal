class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if not hand or not W:
            return False
        _map = defaultdict(list)
        for i in range(len(hand)):
            _map[hand[i]] += [i]
            
        while _map:
            hand = [k for k, _ in list(_map.items())]
            top = min(hand)
            _map[top].pop()
            if not _map[top]:
                del _map[top]
            i = 1
            while hand and i < W:
                top += 1
                if top not in _map:
                    return False
                _map[top].pop()
                if not _map[top]:
                    del _map[top]
                i += 1
            if i < W:
                return False
        return True


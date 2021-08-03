class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand = sorted(hand)
        forward = list(range(1, len(hand)))
        forward.append(None)
        backward = [None]
        backward.extend(list(range(0, len(hand) - 1)))

        ptr = 0
        while ptr is not None:
            firstSkipped = None
            for i in range(W):
                if ptr is None:
                    return False
                currHand = hand[ptr]
                prev = backward[ptr]
                forw = forward[ptr]
                if prev is not None:
                    forward[prev] = forw

                if forw is not None:
                    backward[forw] = prev
                forward[ptr] = backward[ptr] = None
                ptr = forw

                while ptr is not None and hand[ptr] == currHand:
                    if firstSkipped is None:
                        firstSkipped = ptr
                    ptr = forward[ptr]

                if ptr is not None and i != W - 1 and hand[ptr] - 1 != currHand:
                    return False

            if firstSkipped is not None:
                ptr = firstSkipped
        return True

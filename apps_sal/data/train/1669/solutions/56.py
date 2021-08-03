class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()

        def helper(hand):
            # print(hand)
            if not hand:
                return
            if len(hand) % W != 0:
                self.ans = False
                return
            n = len(hand)
            i, k = 0, 0
            prev = hand[0] - 1
            new_hand = []
            while i < n and k < W:
                if hand[i] == prev:
                    new_hand.append(hand[i])
                else:
                    if hand[i] != prev + 1:
                        self.ans = False
                        return
                    else:
                        prev += 1
                        k += 1
                i += 1

            new_hand += hand[i:]
            if not new_hand:
                self.ans = True
                return
            return helper(new_hand)

        helper(hand)
        return self.ans

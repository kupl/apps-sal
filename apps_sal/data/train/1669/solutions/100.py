from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        
        parts = len(hand) / W
        
        cnt = Counter(hand)
        cnt = sorted(cnt.items())
        #print(cnt)
        heapq.heapify(cnt)
        #print(cnt)

        while cnt:
            #print(cnt)
            hand = []
            while len(hand) != W:
                if not cnt:
                    return False

                (card, count) = heapq.heappop(cnt)
                if hand:
                    (last_card, last_count) = hand[-1]
                    if last_card != card - 1:
                        return False
                hand.append((card, count))

            #print(hand)
            for (card, count) in hand:
                count -= 1
                if count:
                    heapq.heappush(cnt, (card, count))

        return True

class Solution:
    import heapq
    def isNStraightHand(self, hand, W):
        heapq.heapify(hand)
        while len(hand) > 0:
            put_back =  []
            count = 0
            prev = hand[0] - 1
            while count < W:
                if len(hand) == 0:
                    return False
                v = heapq.heappop(hand)
                if v != prev + 1:
                    put_back.append(v)
                else:
                    prev = v
                    count += 1

            for element in put_back:
                heapq.heappush(hand, element)
        return True

class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        dic = defaultdict(int)
        for i in range(len(hand)):
            dic[hand[i]] += 1
        for i in range(0, len(hand), W):
            start = min(dic.keys())
            dic[start] -= 1
            if dic[start] == 0:
                del dic[start]
            for i in range(1, W):
                start += 1
                if start not in dic:
                    return False
                dic[start] -= 1
                if dic[start] == 0:
                    del dic[start]
        return True

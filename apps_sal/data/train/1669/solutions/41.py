import collections


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        if W < 1:
            return False

        if len(hand) % W != 0:
            return False

        counter = collections.Counter(hand)
        sorted(counter.items(), key=lambda i: i[0])

        dic = {}
        dic = collections.OrderedDict(sorted(dict(counter).items()))

        while dic:

            dic_list = list(dic.keys())

            base = dic_list[0]

            for i in range(W):
                if base + i not in dic:
                    return False
                dic[base + i] -= 1
                if dic[base + i] == 0:
                    dic.pop(base + i, None)

        return True

from collections import Counter


class Solution:
    '''def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand)<W or len(hand)%W!=0:
            return False
        count = Counter(hand)

        while count:
            sublist = []
            item = min(count)
            sublist.append(item)
            if count[item]==1:
                del count[item]
            else:
                count[item]-=1
            while len(sublist)<W:
                item+=1
                if item not in count:
                    return False
                sublist.append(item+1)
                if count[item]==1:
                    del count[item]
                else:
                    count[item]-=1
        return True'''

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # no need to store the subist themselves
        if len(hand) < W or len(hand) % W != 0:
            return False
        count = Counter(hand)

        while count:
            item = min(count)
            if count[item] == 1:
                del count[item]
            else:
                count[item] -= 1
            i = 1
            while i < W:
                item += 1
                i += 1
                if item not in count:
                    return False
                if count[item] == 1:
                    del count[item]
                else:
                    count[item] -= 1
        return True

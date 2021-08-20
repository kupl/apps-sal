class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        hand.sort()
        count = {}
        for h in hand:
            if h not in count:
                count[h] = 1
            else:
                count[h] += 1
        key = list(count.keys())
        print(count)
        head = 0
        while head < len(key):
            this_key = key[head]
            if count[this_key] == 0:
                head += 1
                continue
            tail = head + 1
            while tail < len(key) and tail < head + W:
                if count[key[tail]] >= count[this_key] and key[tail] == key[tail - 1] + 1:
                    count[key[tail]] -= count[this_key]
                else:
                    return False
                tail += 1
            if tail < head + W:
                return False
            count[this_key] = 0
            head += 1
        return True

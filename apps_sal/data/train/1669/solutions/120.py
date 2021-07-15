class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        
        # we count the frequencies of each card and put it in an ordered dict
        counter = collections.Counter(hand)
        d = collections.OrderedDict(sorted(counter.items()))
        count = 0 # track the number of keys whose value is down to 0
        while count < len(d): 
            group = []
            # go through the ordered dict and put consecutive cards in a group
            # the loop breaks once the size of the group reaches W
            for card in d.keys():
                if d[card] == 0:
                    continue
                if not group or (len(group) < W and group[-1] + 1 == card):
                    group.append(card)
                    d[card] -= 1
                    if d[card] == 0:
                        count += 1
                if len(group) == W:
                    break
            else:
                return False
            
        return True

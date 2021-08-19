class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        ogLen = len(hand)
        if W == 1:
            return True
        counter = Counter(hand)
        counted = [(key, counter[key]) for key in counter]
        counted.sort()
        print(counted)
        heapify(counted)
        groups = []
        group = []
        group.append(heappop(counted))
        tempStorage = set()
        while counted:
            n0 = group[-1]
            if n0[0] + 1 == counted[0][0]:
                n1 = heappop(counted)
            elif counted[0][0] > n0[0] + 1:
                group = []
                group.append(heappop(counted))
                continue
            group.append(n1)
            if len(group) == W:
                groups.append(group)
                for (val, count) in group:
                    count -= 1
                    if count != 0:
                        heappush(counted, (val, count))
                group = []
                if counted:
                    group.append(heappop(counted))
        print((len(groups) * W, ogLen))
        return len(groups) * W == ogLen

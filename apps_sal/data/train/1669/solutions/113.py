class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:

        counts = defaultdict(int)
        for number in hand:
            counts[number] += 1

        ordered_numbers = sorted(counts.keys())
        while counts:
            group = []
            for number in ordered_numbers:

                if number not in counts:
                    continue

                if counts[number] > 0:
                    if group:
                        if group[-1] != number - 1:
                            return False
                    group.append(number)
                    counts[number] -= 1
                else:
                    del counts[number]
                if len(group) == W:
                    break
            if group and len(group) != W:
                return False

        return True

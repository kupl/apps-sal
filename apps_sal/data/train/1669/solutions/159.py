class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W:
            return False
        C = Counter(hand)
        keys = sorted(C.keys())
        output = []
        for i in range(n // W):
            mn = keys[0]
            straight = []
            for j in range(mn, mn + W):
                if j not in keys:
                    return False
                else:
                    C[j] -= 1
                    straight.append(j)
                    if C[j] == 0:
                        del C[j]
                        keys.remove(j)
            output.append(straight)
        print(output)
        return True

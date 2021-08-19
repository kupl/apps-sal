class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        # if len(hand) != W**2:
        #    return False

        counted = {}
        for i in hand:
            if i not in counted:
                counted[i] = 0
            counted[i] += 1

        def containStrait(numbers, counted, W):
            #print(numbers, counted)
            if len(counted) == 0:
                return True
            if len(numbers) < W:
                return False

            if numbers[W - 1] - numbers[0] > W:
                counted.pop(numbers[0])
                numbers.remove(numbers[0])
                # return containStrait(numbers, counted, W, count)
            else:
                for i in reversed(range(W)):
                    counted[numbers[i]] -= 1
                    if counted[numbers[i]] == 0:
                        counted.pop(numbers[i])
                        numbers.remove(numbers[i])
                #count -= 1
            return containStrait(numbers, counted, W)

        numbers = sorted(counted.keys())
        return containStrait(numbers, counted, W)

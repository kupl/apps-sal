class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counted = {}
        for i in hand:
            if i not in counted:
                counted[i] = 0
            counted[i] += 1

        def containStrait(numbers, counted, W):
            if len(counted) == 0:
                return True
            if len(numbers) < W:
                return False
            if numbers[W - 1] - numbers[0] > W:
                counted.pop(numbers[0])
                numbers.remove(numbers[0])
            else:
                min_count = sys.maxsize
                for i in reversed(range(W)):
                    if counted[numbers[i]] < min_count:
                        min_count = counted[numbers[i]]
                for i in reversed(range(W)):
                    counted[numbers[i]] -= min_count
                    if counted[numbers[i]] == 0:
                        counted.pop(numbers[i])
                        numbers.remove(numbers[i])
            return containStrait(numbers, counted, W)
        numbers = sorted(counted.keys())
        return containStrait(numbers, counted, W)

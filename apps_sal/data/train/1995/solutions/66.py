class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickups = sorted([lst[:2] for lst in trips], key=lambda lst: lst[1])
        dropoffs = sorted([lst[::2] for lst in trips], key=lambda lst: lst[1])
        print(pickups, dropoffs)

        currentCap = 0
        i, j = 0, 0
        nextP, nextD = pickups[0], dropoffs[0]
        while i < len(pickups):
            if nextP[1] < nextD[1] or not nextD:
                currentCap += nextP[0]
                i += 1
                if i < len(pickups):
                    nextP = pickups[i]
                else:
                    nextP = None
            elif nextP[1] > nextD[1] or not nextP:
                currentCap -= nextD[0]
                j += 1
                if j < len(dropoffs):
                    nextD = dropoffs[j]
                else:
                    nextD = None
            else:
                currentCap += nextP[0] - nextD[0]
                i += 1
                j += 1
                if i < len(pickups):
                    nextP = pickups[i]
                else:
                    nextP = None
                if j < len(dropoffs):
                    nextD = dropoffs[j]
                else:
                    nextD = None

            print(i, j, currentCap)
            if currentCap > capacity:
                return False
        return True

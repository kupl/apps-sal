class Solution:
    def checkMultiple(self, num, maxLCM):
        d = 2
        while d <= maxLCM:
            if num % d == 0:
                return True
            d += 1
        return False

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        intCnt = {}
        for num in deck:
            if num not in intCnt:
                intCnt[num] = 0
            intCnt[num] += 1
        i = 1
        n = len(intCnt)
        cnts = list(intCnt.values())
        cnts.sort()
        leastDiff = None
        leastCnt = cnts[0]
        while i < n:
            curDiff = cnts[i] - cnts[i - 1]
            if leastDiff == None or curDiff < leastDiff:
                leastDiff = curDiff
            if cnts[i] < leastCnt:
                leastCnt = cnts[i]
            i += 1
        if leastDiff == 0 or leastDiff == None:
            leastDiff = leastCnt
        for num in intCnt:
            if intCnt[num] < 2 or leastDiff <= 1 or not self.checkMultiple(intCnt[num], leastDiff):
                return False
        return True

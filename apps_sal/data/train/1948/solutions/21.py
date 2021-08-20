import math


class Solution:

    def numPoints(self, points: List[List[int]], r: int) -> int:
        self.total = len(points)
        maxPoints = 0
        for i in range(self.total):
            maxPoints = max(maxPoints, self.numPointsInCircle(points, r, i))
        return maxPoints

    def numPointsInCircle(self, points, r, chosenIndex):
        maxPoints = 0
        enterList = []
        exitList = []
        numberPoints = 0
        for i in range(self.total):
            answer = self.computeRange(points, r, chosenIndex, i)
            if answer != None:
                if len(answer) == 0:
                    numberPoints += 1
                else:
                    (enterAngle, exitAngle) = answer
                    enterList.append(enterAngle)
                    exitList.append(exitAngle)
                    if enterAngle > exitAngle:
                        numberPoints += 1
        exitList.sort()
        enterList.sort()
        maxPoints = numberPoints
        exitCounter = 0
        enterCounter = 0
        pointsToCheck = len(exitList)
        while max(exitCounter, enterCounter) < pointsToCheck:
            currentExit = exitList[exitCounter]
            currentEnter = enterList[enterCounter]
            if currentEnter <= currentExit:
                numberPoints += 1
                maxPoints = max(maxPoints, numberPoints)
                enterCounter += 1
            else:
                numberPoints -= 1
                exitCounter += 1
        while exitCounter < pointsToCheck:
            numberPoints -= 1
            exitCounter += 1
        while enterCounter < pointsToCheck:
            numberPoints += 1
            maxPoints = max(maxPoints, numberPoints)
            enterCounter += 1
        return maxPoints

    def computeRange(self, points, r, chosenIndex, otherIndex):
        chosenPair = points[chosenIndex]
        otherPair = points[otherIndex]
        if chosenPair == otherPair:
            return []
        else:
            distance = self.distanceBetweenPoints(chosenPair, otherPair)
            if distance > 2 * r:
                return None
            else:
                angleOne = self.computeAngle(chosenPair, otherPair)
                angleTwo = math.acos(distance / (2 * r))
                exit = angleOne + angleTwo
                exit = exit - 2 * math.pi if exit >= math.pi else exit
                enter = angleOne - angleTwo
                enter = enter + 2 * math.pi if enter < -math.pi else enter
                return [enter, exit]

    def computeAngle(self, pairOne, pairTwo):
        (x1, y1) = pairOne
        (x2, y2) = pairTwo
        return math.atan2(y2 - y1, x2 - x1)

    def numberPointsStart(self, enterList, exitList):
        pass

    def distanceBetweenPoints(self, pairOne, pairTwo):
        (x1, y1) = pairOne
        (x2, y2) = pairTwo
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

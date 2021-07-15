def spidey_swings(buildings):
    answer = []
    corners = []
    sumWidths = 0
    for (height, width) in buildings:
        sumWidths += width
        corners.append((sumWidths, height))
    xSpidey, ySpidey = 0, 50
    while True:
        maxAvgYield, bestDist, bestX, bestReached = 0, None, None, False
        minRope = 9999
        xCornerLast = 0
        for xCorner, yCorner in corners:
            if xCorner <= xSpidey:
                xCornerLast = xCorner
                continue
            for x in range(max(xSpidey, xCornerLast), xCorner + 1):
                xDist = x - xSpidey
                yDist = yCorner - ySpidey
                lenRope = (xDist ** 2 + yDist ** 2) ** 0.5
                if yCorner - lenRope < 20:
                    break
                dist = xDist * 2
                reached = (xSpidey + dist >= sumWidths)
                avgYield = dist / lenRope
                if not reached and maxAvgYield < avgYield:
                    maxAvgYield = avgYield
                    bestDist = dist
                    bestX = x
                elif not bestReached and reached:
                    minRope = lenRope
                    bestDist = dist
                    bestX = x
                    bestReached = reached
                elif bestReached and reached and minRope > lenRope:
                    minRope = lenRope
                    bestDist = dist
                    bestX = x
            xCornerLast = xCorner
        answer.append(bestX)
        xSpidey += bestDist
        if xSpidey >= sumWidths:
            break
    return answer

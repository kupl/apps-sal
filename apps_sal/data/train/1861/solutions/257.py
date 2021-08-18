class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        xAxis = {}
        yAxis = {}
        minArea = None

        for point in points:
            if xAxis.get(point[0]):
                xAxis[point[0]].append(point[1])
            else:
                xAxis[point[0]] = [point[1]]

            if yAxis.get(point[1]):
                yAxis[point[1]].append(point[0])
            else:
                yAxis[point[1]] = [point[0]]

        for point in points:
            topLeft = xAxis[point[0]]
            bottomRight = yAxis[point[1]]

            for tlPoint in topLeft:
                if tlPoint == point[1]:
                    continue

                possibleTopRight = yAxis[tlPoint]
                topRight = [value for value in possibleTopRight if value in bottomRight and value != point[0]]

                for trPoint in topRight:
                    area = abs((trPoint - point[0]) * (tlPoint - point[1]))

                    if area != 0 and (minArea == None or area < minArea):
                        minArea = area

            xAxis[point[0]].remove(point[1])
            yAxis[point[1]].remove(point[0])

        return 0 if minArea == None else minArea

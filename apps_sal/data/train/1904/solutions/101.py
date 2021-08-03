class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        arr = self.sortPoints(points)
        return arr[:K]

    def sortPoints(self, points):
        if len(points) <= 1:
            return points
        mid = len(points) // 2
        left = self.sortPoints(points[:mid])
        right = self.sortPoints(points[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        arr, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            xLeft, yLeft = left[i][0], left[i][1]
            xRight, yRight = right[j][0], right[j][1]
            leftDis = xLeft * xLeft + yLeft * yLeft
            rightDis = xRight * xRight + yRight * yRight

            if leftDis < rightDis:
                arr.append(left[i])
                i += 1
            elif rightDis < leftDis:
                arr.append(right[j])
                j += 1
            else:
                arr.append(left[i])
                arr.append(right[j])
                i, j = i + 1, j + 1
        while i < len(left):
            arr.append(left[i])
            i += 1
        while j < len(right):
            arr.append(right[j])
            j += 1
        return arr

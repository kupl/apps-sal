class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = lambda x, y: sqrt(x**2 + y**2)
        k = 0
        output = []
        for s in sorted(points, key=lambda x: distance(x[0], x[1])):
            if k < K:
                output.append(s)
            else:
                break
            k += 1
        return output

class Solution:

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        elif start > destination:
            (start, destination) = (destination, start)
        cw = 0
        for i in range(start, destination):
            cw += distance[i]
        ccw = 0
        n = len(distance)
        for i in range(destination, start + n):
            ccw += distance[i % n]
        return min(cw, ccw)

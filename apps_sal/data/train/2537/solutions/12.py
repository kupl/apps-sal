class Solution:

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        fdistance = 0
        sdistance = 0
        n = len(distance)
        for i in range(start, start + n):
            if i % n == destination:
                break
            fdistance += distance[i % n]
        for i in range(destination, destination + n):
            if i % n == start:
                break
            sdistance += distance[i % n]
        return fdistance if fdistance < sdistance else sdistance

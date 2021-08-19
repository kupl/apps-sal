class Solution:

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        p1 = start % n
        p2 = destination % n
        d1 = 0
        d2 = 0
        while p1 != destination and p2 != start:
            d1 += distance[p1]
            d2 += distance[p2]
            p1 = (p1 + 1) % n
            p2 = (p2 + 1) % n
        if p1 == destination:
            return d1
        return d2

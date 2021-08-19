class Solution:

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        if start > destination:
            (start, destination) = (destination, start)
        assert start != destination
        return min(sum(distance[start:destination]), sum(distance[:start] + distance[destination:]))

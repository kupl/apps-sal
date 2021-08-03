class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        total = sum(distance)

        journey = 0
        while start % len(distance) != destination:
            journey += distance[start % len(distance)]
            start += 1

        return min(journey, total - journey)

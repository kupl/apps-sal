class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if start > destination:
            start, destination = destination, start

        sum1 = sum(distance[start:destination])
        sum2 = sum(distance) - sum1

        return min(sum1, sum2)

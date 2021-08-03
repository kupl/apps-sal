class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        distance += [0]
        for i in range(len(distance) - 2, -1, -1):
            distance[i] += distance[i + 1]

        d = abs(distance[start] - distance[destination])

        return min(d, distance[0] - d)

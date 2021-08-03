class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise = 0
        i = start
        while i != destination:
            clockwise += distance[i]
            if i == len(distance) - 1:
                i = 0
            else:
                i += 1

        i = start
        counterclockwise = 0
        while i != destination:

            if i == 0:
                i = len(distance) - 1
            else:
                i -= 1
            counterclockwise += distance[i]

        return min(clockwise, counterclockwise)

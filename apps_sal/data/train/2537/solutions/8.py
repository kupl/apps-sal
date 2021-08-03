class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0

        if start > destination:
            start, destination = destination, start

        increase = start
        decrease = start
        right = 0
        left = 0

        while True:
            index = (increase) % len(distance)
            increase += 1
            if(index == destination):
                break
            right += distance[index]

        while True:
            decrease -= 1
            index = (decrease) % len(distance)
            left += distance[index]
            if(index == destination):
                break

        return min(left, right)

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        num = len(distance)
        if start <= destination:
            dis1 = sum(distance[start:destination])
            dis2 = sum(distance[destination:]) + sum(distance[:start])
        elif start > destination:
            dis1 = sum(distance[start:]) + sum(distance[:destination])
            dis2 = sum(distance[destination:start])

        return min(dis1, dis2)

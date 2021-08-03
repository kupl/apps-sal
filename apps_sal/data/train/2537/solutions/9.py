class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        s_d = 0
        d_s = 0
        d_sd = []

        if (start < destination):
            d_sd = distance[start:destination]

        if (start >= destination):
            d_sd = distance[:destination] + distance[start:]

        for x in range(len(d_sd)):
            s_d += d_sd[x]

        d_s = sum(distance) - s_d

        return min(s_d, d_s)

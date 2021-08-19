from typing import List
from math import pow


class Solution:
    def start_to_end_traverasal(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        n: int = len(distance)
        total: int = 0
        index: int = start
        end: int = int((destination - 1 + n) % n)
        while True:
            total += distance[index]
            if index == end:
                break
            else:
                index += 1
                if index == n:
                    index = 0
        return total

    def end_to_start_traverasal(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        return self.start_to_end_traverasal(distance, destination, start)

    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        n: int = len(distance)
        assert 1 <= n and n <= pow(10, 4)
        assert destination < n
        assert 0 <= start

        clockwise_total: int = self.start_to_end_traverasal(
            distance, start, destination
        )
        counterclockwise_total: int = self.end_to_start_traverasal(
            distance, start, destination
        )

        # compare which path took less time
        return min(clockwise_total, counterclockwise_total)

from typing import Dict, List
from math import floor

class TimeMap:

    def __init__(self):
        self.data: Dict[str, List[(int, str)]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return \"\"

        values = self.data[key]
        start = 0
        end = len(values)

        while start < end:
            mid = floor((start + end) / 2)
            mid_timestamp, mid_value = values[mid]

            if timestamp == mid_timestamp:
                return mid_value
            elif timestamp < mid_timestamp:
                end = mid
            else:
                start = mid + 1

        largest_index_less_than = start - 1
        if largest_index_less_than < 0:
            return \"\"

        _, value = values[largest_index_less_than]
        return value

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        n = len(trips)

        sorted_trips = sorted(trips, key=lambda t: t[1])

        min_idx = sorted_trips[0][1]
        max_idx = max([t[2] for t in sorted_trips])

        merged = [0 for _ in range(max_idx + 1)]

        for num_passenger, start_idx, end_idx in sorted_trips:
            for idx in range(start_idx, end_idx):
                merged[idx] += num_passenger
                if merged[idx] > capacity:
                    return False

        return True

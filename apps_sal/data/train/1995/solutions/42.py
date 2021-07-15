class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips: List[[num_passengers, start_idx, end_idx]]
        # for each position, count number of people required
        
        n = len(trips)
        
        # 1. arrange trips by start date
        sorted_trips = sorted(trips, key=lambda t: t[1])
        
        # 2. for min_idx, max_idx keep track of all active trips overlapping
        min_idx = sorted_trips[0][1]
        max_idx = max([t[2] for t in sorted_trips])
        
        merged = [0 for _ in range(max_idx + 1)]
        
        # base case
        for num_passenger, start_idx, end_idx in sorted_trips:
            for idx in range(start_idx, end_idx):
                merged[idx] += num_passenger
                if merged[idx] > capacity:
                    # print(f\"merged={merged}; idx={idx}\")
                    return False
        
        return True
            


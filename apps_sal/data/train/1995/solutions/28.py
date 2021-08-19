class Solution:

    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        sorted_trips = sorted(trips, key=lambda x: x[1])
        in_trip = [sorted_trips[0]]
        cap = capacity - sorted_trips[0][0]
        cur_time = 0
        i = 1
        while i < len(sorted_trips):
            waiting_passenger = sorted_trips[i]
            if not in_trip:
                cap -= waiting_passenger[0]
                in_trip.append(waiting_passenger)
                i += 1
            else:
                first_passenger = in_trip[0]
                if waiting_passenger[1] >= first_passenger[2]:
                    in_trip.pop(0)
                    cap += first_passenger[0]
                elif cap >= waiting_passenger[0]:
                    cap -= waiting_passenger[0]
                    in_trip.append(waiting_passenger)
                    in_trip = sorted(in_trip, key=lambda x: x[2])
                    i += 1
                else:
                    return False
        return True

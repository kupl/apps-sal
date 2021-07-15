def days_represented(trips):
    trips.sort()
    print(trips)
    previous_end = trips[0][1]
    days = previous_end - trips[0][0] + 1
    trips.pop(0)
    for trip in trips:
        start, end = trip
        if start > previous_end:
            days += end-start+1
            previous_end = end
        elif end > previous_end:
            days += end - previous_end
            previous_end = end
    return days

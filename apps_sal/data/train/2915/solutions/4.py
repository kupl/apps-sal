def check_availability(schedule, now):
    return next((end for start, end in schedule if start <= now < end), True)

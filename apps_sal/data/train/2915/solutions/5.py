def check_availability(schedule, current_time):
    return next((stop for start, stop in schedule if start <= current_time < stop), True)

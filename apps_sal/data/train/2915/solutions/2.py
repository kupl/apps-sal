def check_availability(schedule, current_time):
    return next((end for start,end in schedule if start < current_time < end), True)

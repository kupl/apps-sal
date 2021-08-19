def check_availability(schedule, current_time):
    for (start, stop) in schedule:
        if start <= current_time < stop:
            return stop
    return True

def check_availability(schedule, current_time):
    for time in schedule:
        if time[0] <= current_time < time[1]:
            return time[1]
    return True

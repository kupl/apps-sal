def check_availability(schedule, current_time):
    for tb, te in schedule:
        if tb <= current_time < te:
            return te
    return True

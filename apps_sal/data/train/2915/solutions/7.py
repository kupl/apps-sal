def check_availability(schedule, current_time):
    for s, e in schedule:
        if s <= current_time < e: return e
    return True

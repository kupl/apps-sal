def check_availability(schedule, current_time):
    for meeting in schedule: return meeting[1] if meeting[0] <= current_time < meeting[1] else True
    return True

def day_plan(hours, tasks, duration):
    breaks = (hours * 60 - tasks * duration) / (tasks - 1) if tasks > 1 else 0
    if breaks < 0:
        return "You're not sleeping tonight!"
    return ([duration, round(breaks)] * tasks)[:-1]

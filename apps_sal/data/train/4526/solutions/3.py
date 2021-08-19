def day_plan(hours, tasks, duration):
    if tasks < 2:
        return [duration] * tasks
    elif tasks * duration / 60 > hours:
        return "You're not sleeping tonight!"
    else:
        r = round((hours * 60 - tasks * duration) / (tasks - 1))
        return [duration, r] * (tasks - 1) + [duration]

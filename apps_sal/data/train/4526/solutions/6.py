def day_plan(hours, tasks, duration):
    if tasks == 0: return []
    if tasks == 1: return [duration]
    stop = round((hours*60 - duration*tasks) / (tasks - 1))
    if stop < 0: return "You're not sleeping tonight!"
    res = [None]*(2*tasks-1)
    res[::2] = [duration]*tasks
    res[1::2] = [stop]*(tasks-1)
    return res

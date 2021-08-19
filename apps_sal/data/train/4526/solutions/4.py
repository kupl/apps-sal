def day_plan(hours, tasks, duration):
    break_time = hours * 60 - tasks * duration
    if break_time < 0:
        return "You're not sleeping tonight!"
    else:
        schedule = [0] * (2 * tasks - 1)
        schedule[::2] = [duration] * tasks
        schedule[1::2] = [round(break_time / (tasks - 1 + 1e-09))] * (tasks - 1)
        return schedule

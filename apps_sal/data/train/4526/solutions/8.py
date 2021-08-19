def day_plan(hours, tasks, duration):
    total_minutes = hours * 60
    tasks_minutes = tasks * duration
    if tasks_minutes > total_minutes:
        return "You're not sleeping tonight!"
    brk = round((total_minutes - tasks_minutes) / (tasks - 1)) if tasks > 1 else 0
    return [brk if i % 2 else duration for i in range(2 * tasks - 1)]

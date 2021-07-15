def day_plan(hours, tasks, duration):
    mins = hours * 60
    task_mins = tasks * duration
    relaxation = (mins - task_mins) / max(1, (tasks - 1))
    if relaxation < 0:
        return "You're not sleeping tonight!"
    task_list = ([duration, round(relaxation, 0)] * tasks)[:-1]
    return task_list

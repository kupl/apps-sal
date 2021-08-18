def day_plan(hours, tasks, duration):
    at = tasks * duration
    tb = (hours * 60) - at
    plan = []
    if tb < 0:
        return "You're not sleeping tonight!"
    elif tasks == 0:
        return plan
    elif tasks == 1:
        plan = [duration]
    else:
        plan = [duration]
        bt = round(tb / (tasks - 1))
        for i in range(tasks - 1):
            plan.append(bt)
            plan.append(duration)
    return plan

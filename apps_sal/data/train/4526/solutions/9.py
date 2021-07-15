def day_plan(hours, tasks, duration):
    minutes=hours*60
    if tasks*duration>minutes:return "You're not sleeping tonight!"
    elif tasks==1:return [duration]
    elif tasks==0:return []
    break_length = round((minutes-tasks*duration)/(tasks-1))
    return [duration,break_length]*(tasks-1)+[duration]

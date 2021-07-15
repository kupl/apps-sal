def day_plan(hours, tasks, duration):
    td, hm, tmo = tasks * duration, hours * 60, tasks - 1
    if td > hm: return "You're not sleeping tonight!"
    arr = [0] * (tasks + tmo)
    arr[::2], arr[1::2] = [duration] * tasks, [round((hm - td) / (tmo or 1))] * tmo
    return arr


def travel(total_time, run_time, rest_time, speed):
    cycle, left = divmod(total_time, run_time + rest_time)
    return cycle * run_time * speed + min(left, run_time) * speed

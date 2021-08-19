def travel(total_time, run_time, rest_time, speed):
    (x, y) = divmod(total_time, run_time + rest_time)
    return (x * run_time + min(y, run_time)) * speed

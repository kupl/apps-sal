def travel(total_time, run_time, rest_time, speed):
    (d, m) = divmod(total_time, run_time + rest_time)
    return (d * run_time + min(m, run_time)) * speed

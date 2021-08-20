def travel(total_time, run_time, rest_time, speed):
    (runs, extra) = divmod(total_time, run_time + rest_time)
    return (runs * run_time + min(extra, run_time)) * speed

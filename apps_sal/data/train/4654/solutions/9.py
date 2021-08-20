def travel(total_time, run_time, rest_time, speed):
    (s, is_running) = (0, True)
    while total_time:
        if is_running:
            s += min(total_time, run_time) * speed
        total_time -= min(total_time, run_time) if is_running else min(rest_time, total_time)
        is_running = not is_running
    return s

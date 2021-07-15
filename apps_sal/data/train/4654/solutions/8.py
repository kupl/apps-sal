def travel(total_time, run_time, rest_time, speed):
    run_periods = float(total_time) / (run_time + rest_time)
    last_run_time = min(run_periods-int(run_periods), float(run_time)/(run_time + rest_time))*(run_time + rest_time)
    total_run_time = int(run_periods)*run_time + last_run_time
    return round(total_run_time * speed)


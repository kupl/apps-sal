def travel(total_time, run_time, rest_time, speed):
    return speed * (run_time * (total_time // (run_time + rest_time)) + min(run_time, total_time % (run_time + rest_time)))

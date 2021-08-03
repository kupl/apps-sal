def travel(total_time, run_time, rest_time, speed):
    cycles, remaining = divmod(total_time, run_time + rest_time)
    last_run = min(remaining, run_time)
    return (cycles * run_time + last_run) * speed


def travel(total, run, rest, speed):
    return ((total // (run + rest)) * run + min(total % (run + rest), run)) * speed

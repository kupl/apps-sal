def travel(total_time, run_time, rest_time, speed):
    av_speed = (speed * run_time) / (run_time + rest_time)
    av_time = total_time // (run_time + rest_time)
    r_time = (total_time - av_time * (run_time + rest_time))
    return round(av_time * (run_time + rest_time) * av_speed + run_time * speed) if run_time < r_time else round(av_time * (run_time + rest_time) * av_speed + r_time * speed)

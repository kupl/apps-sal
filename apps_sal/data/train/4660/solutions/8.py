def can_i_play(now_hour, start_hour, end_hour):
    end = end_hour+24 if start_hour > end_hour else end_hour
    now_hour = now_hour if now_hour >= start_hour else now_hour+24
    return start_hour <= now_hour < end

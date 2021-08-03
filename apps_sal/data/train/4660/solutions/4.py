def can_i_play(now_hour, start_hour, end_hour):
    if end_hour < start_hour:
        end_hour += 24
    if now_hour < start_hour:
        now_hour += 24
    return True if now_hour >= start_hour and now_hour < end_hour else False

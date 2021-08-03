def can_i_play(now_hour, start_hour, end_hour):
    return 0 <= (now_hour - start_hour) % 24 < (end_hour - start_hour) % 24

from datetime import time


def can_i_play(now_hour, start_hour, end_hour):
    return end_hour < start_hour <= now_hour or (end_hour > now_hour and start_hour > end_hour) or start_hour <= now_hour < end_hour

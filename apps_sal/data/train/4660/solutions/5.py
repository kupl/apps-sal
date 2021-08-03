from operator import and_, or_


def can_i_play(now_hour, start_hour, end_hour):
    return (and_, or_)[end_hour < start_hour](start_hour <= now_hour, now_hour < end_hour)

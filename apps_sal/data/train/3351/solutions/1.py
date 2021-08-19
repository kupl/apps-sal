from bisect import bisect_right as bisect
MEDALS = ['Gold', 'Silver', 'Bronze', 'None']


def evil_code_medal(user_time, *times):
    return MEDALS[bisect(times, user_time)]

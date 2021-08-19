def evil_code_medal(user_time, gold, silver, bronze):
    user_seconds = time_to_seconds(user_time)
    if user_seconds < time_to_seconds(gold):
        return 'Gold'
    elif user_seconds < time_to_seconds(silver):
        return 'Silver'
    elif user_seconds < time_to_seconds(bronze):
        return 'Bronze'
    else:
        return 'None'


def time_to_seconds(time):
    (hours, minutes, seconds) = time.split(':')
    return 3600 * int(hours) + 60 * int(minutes) + int(seconds)

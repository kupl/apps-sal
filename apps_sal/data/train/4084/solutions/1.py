def alex_mistakes(katas, time):
    mistakes = 0
    pushup_time = 5
    time_left = time - katas * 6
    while time_left >= pushup_time:
        time_left -= pushup_time
        pushup_time *= 2
        mistakes += 1
    return mistakes

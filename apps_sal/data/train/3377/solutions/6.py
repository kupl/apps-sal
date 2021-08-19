locale = 'midnight one two three four five six seven eight nine ten eleven twelve thirteen fourteen quarter sixteen seventeen eighteen nineteen twenty'.split()
locale += [f'{locale[-1]} {digit}'.rstrip() for digit in locale[1:10]] + "half, o'clock, minutes, past , to ".split(',')


def solve(time):
    (preposition, (hour, minute)) = (-2, list(map(int, time.split(':'))))
    if minute > 30:
        (preposition, hour, minute) = (preposition + 1, (hour + 1) % 24, 60 - minute)
    if hour > 12:
        hour -= 12
    if not minute:
        return f'{locale[hour]}{locale[-4] * (hour > 0)}'
    return f'{locale[minute]}{locale[-3][:-(minute == 1) or None] * (minute not in (15, 30))}{locale[preposition]}{locale[hour]}'

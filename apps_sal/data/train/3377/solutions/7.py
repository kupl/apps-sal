MINUTES = (
    'zero,one,two,three,four,five,six,seven,eight,nine,'
    + 'ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,'
    + 'twenty'
).split(',')
MINUTES.extend([f'twenty {n}' for n in MINUTES[1:10]])

# Should be
# HOURS = ['midnight'] + MINUTES[1:12] + ['midday'] + MINUTES[1:12]
HOURS = ['midnight'] + MINUTES[1:13] + MINUTES[1:12]

# Special cases: minutes -> (string template, hour offset)
QUARTERS = {
    0: ("{h} o'clock", 0),
    15: ('quarter past {h}', 0),
    30: ('half past {h}', 0),
    45: ('quarter to {h}', 1),
}


def solve(time):
    hh, mm = list(map(int, time.split(':')))
    h = HOURS[hh]
    h1 = HOURS[(hh + 1) % 24]

    if mm in QUARTERS:
        # On an hour, quarter or half
        template, offset = QUARTERS[mm]
        if mm == 0 and hh == 0:  # 12:00 should really be 'midday' too
            return h
        return template.format(h=h if offset == 0 else h1)

    if mm < 30:
        # x minute(s) past y
        return f"{MINUTES[mm]} minute{'' if mm == 1 else 's'} past {h}"

    # x minute(s) to y
    mm = 60 - mm
    return f"{MINUTES[mm]} minute{'' if mm == 1 else 's'} to {h1}"

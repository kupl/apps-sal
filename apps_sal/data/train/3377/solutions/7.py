MINUTES = ('zero,one,two,three,four,five,six,seven,eight,nine,' + 'ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,' + 'twenty').split(',')
MINUTES.extend([f'twenty {n}' for n in MINUTES[1:10]])
HOURS = ['midnight'] + MINUTES[1:13] + MINUTES[1:12]
QUARTERS = {0: ("{h} o'clock", 0), 15: ('quarter past {h}', 0), 30: ('half past {h}', 0), 45: ('quarter to {h}', 1)}


def solve(time):
    (hh, mm) = list(map(int, time.split(':')))
    h = HOURS[hh]
    h1 = HOURS[(hh + 1) % 24]
    if mm in QUARTERS:
        (template, offset) = QUARTERS[mm]
        if mm == 0 and hh == 0:
            return h
        return template.format(h=h if offset == 0 else h1)
    if mm < 30:
        return f"{MINUTES[mm]} minute{('' if mm == 1 else 's')} past {h}"
    mm = 60 - mm
    return f"{MINUTES[mm]} minute{('' if mm == 1 else 's')} to {h1}"

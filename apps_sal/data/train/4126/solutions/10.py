from math import floor


def what_time_is_it(angle):
    (hr, mt) = divmod(12 * angle, 360)
    if hr < 1:
        hr = 12
    hr = f'{floor(hr)}'.rjust(2, '0')
    mt = f'{floor(mt) // 6}'.rjust(2, '0')
    return f'{hr}:{mt}'

from math import sin, pi


def scroller(text, amp, period):
    ret = []
    for m, i in enumerate(text):
        ret.append('{}{}'.format(' ' * round(amp + (amp * sin(m * pi * 2/ period))), i))
    return '\n'.join(ret)

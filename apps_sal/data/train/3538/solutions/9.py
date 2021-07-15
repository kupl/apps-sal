from math import sin, pi


def sin_gen(text, amp, period):
    for n, i in enumerate(text):
        yield int(round(amp + amp * sin((2 * pi / period) * n)))


def scroller(text, amp, period):
    return "\n".join([" " * y + text[i] for i, y in enumerate(sin_gen(text, amp, period))])

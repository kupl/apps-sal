from math import sin, pi


def scroller(text, amp, period):
    ans = [f"{' ' * round(amp + sin(2 * pi / period * i) * amp)}{ch}" for (i, ch) in enumerate(text)]
    return '\n'.join(ans)

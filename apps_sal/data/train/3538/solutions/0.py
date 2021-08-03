from math import pi, sin


def scroller(text, amp, period):
    return '\n'.join(' ' * (amp + int(round(sin(i * 2 * pi / period) * amp))) + c for i, c in enumerate(text))

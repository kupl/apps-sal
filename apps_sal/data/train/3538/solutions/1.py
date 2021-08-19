import math


def scroller(text, amp, period):

    def l(i, c):
        return ' ' * (amp + i) + c + '\n'
    return ''.join([l(round(amp * math.sin(2 * math.pi * (i / period))), text[i]) for i in range(len(text))])[:-1]

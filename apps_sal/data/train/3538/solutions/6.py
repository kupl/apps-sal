import math


def scroller(text, amp, period):
    phi = 2 * math.pi / period
    ans = []
    for (i, e) in enumerate(text):
        x = math.sin(phi * i) + 1
        t = round(x * amp)
        temp = ' ' * int(t) + e
        ans.append(temp)
    return '\n'.join(ans)

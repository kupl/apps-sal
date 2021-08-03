from math import sin, pi


def scroller(text, amp, period):
    step = 2 * pi / period
    output = []

    for i, char in enumerate(text):
        line = ' ' * (int(round(amp * sin(step * i) + amp))) + char
        output.append(line)

    return '\n'.join(output)

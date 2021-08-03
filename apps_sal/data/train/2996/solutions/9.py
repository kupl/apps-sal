import re


def how_much_coffee(events):
    c = 0
    for event in events:
        m = re.match(r'^(cw|dog|cat|movie)$', event, re.I)
        if m:
            if event.isupper():
                c += 2
            else:
                c += 1
    if c <= 3:
        return c
    else:
        return "You need extra sleep"

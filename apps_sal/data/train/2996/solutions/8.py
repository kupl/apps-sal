import re


def how_much_coffee(events):
    if events:
        a = sum([1 if re.match('^(cw|cat|dog|movie)$', i) else 0 for i in events])
        b = sum([2 if re.match('^(CW|CAT|DOG|MOVIE)$', i) else 0 for i in events])
        return 'You need extra sleep' if a + b > 3 else a + b
    return 0

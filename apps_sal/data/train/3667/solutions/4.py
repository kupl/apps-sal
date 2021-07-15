import re
def mid_endian(n):
    t = f'{n:X}'
    t = '0' + t if len(t) % 2 else t

    odds, evens = [], []
    for i, f in enumerate(re.findall(r'..', t), start=1):
        if i % 2:
            odds.append(f)
        else:
            evens.append(f)
    return ''.join(list(reversed(evens)) + odds)

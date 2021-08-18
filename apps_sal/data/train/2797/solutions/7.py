count = {chr(n): 2 + i % 3 for i, n in enumerate(range(ord('a'), ord('s')))}
count.update({chr(n): 2 + i % 3 for i, n in enumerate(range(ord('t'), ord('z')))})
count.update({str(n)[-1]: 1 for i, n in enumerate(range(1, 11))})
count.update({'s': 5, 'z': 5, '*': 1, '


def mobile_keyboard(s):
    return sum(count[c] for c in s)

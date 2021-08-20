def find(str, ch):
    for (i, ltr) in enumerate(str):
        if ltr == ch:
            yield i


def solve(s):
    new_s = s[::-1].replace(' ', '')
    for idx in list(find(s, ' ')):
        new_s = new_s[:idx] + ' ' + new_s[idx:]
    return new_s

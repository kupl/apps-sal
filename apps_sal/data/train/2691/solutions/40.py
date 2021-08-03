def solve(s):
    max = float('-inf')
    s = list(s)
    word = ' '
    for ch in s:
        if ch.isnumeric():
            word += ch
        if not ch.isnumeric():
            word += ' '
    lists = word.split(' ')
    for value in lists:
        if value.isnumeric():
            if int(value) > max:
                max = int(value)
        else:
            pass
    return max

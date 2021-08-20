NUM = 'midnight one two three four five six seven eight nine\n  ten eleven twelve thir_ four_ fif_ six_ seven_ eigh_ nine_\n  twenty'.replace('_', 'teen').split()
for n in range(1, 10):
    NUM.append(f'twenty {NUM[n]}')


def solve(time):
    (hh, mm) = map(int, time.split(':'))
    if mm > 30:
        hh += 1
    hour = NUM[hh % 12] if hh % 12 else NUM[hh % 24]
    if mm == 0:
        min = ''
    elif mm == 15:
        min = 'quarter past '
    elif mm == 30:
        min = 'half past '
    elif mm == 45:
        min = 'quarter to '
    elif 0 < mm < 30:
        min = f"{NUM[mm]} minute{('s' if mm > 1 else '')} past "
    else:
        min = f"{NUM[60 - mm]} minute{('s' if mm < 59 else '')} to "
    return min + hour + (" o'clock" if mm == 0 and hh > 0 else '')

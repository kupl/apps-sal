NUMS = [''] + '''
one two three four five six seven eight nine ten
eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty
'''.split()
NUMS += [f'twenty {NUMS[i]}' for i in range(1, 10)]
NUMS += ['thirty']

MINUTES = [f'{x} minutes' for x in NUMS]
MINUTES[1], MINUTES[15], MINUTES[30] = 'one minute', 'quarter', 'half'

HOURS = ['midnight'] + NUMS[1:13] + NUMS[1:12]


def solve(time):
    h, m = map(int, time.split(':'))
    if h == m == 0:
        return 'midnight'
    if m == 0:
        return f"{HOURS[h]} o'clock"
    elif m <= 30:
        return f'{MINUTES[m]} past {HOURS[h]}'
    else:
        h = (h + 1) % 24
        return f'{MINUTES[60 - m]} to {HOURS[h]}'

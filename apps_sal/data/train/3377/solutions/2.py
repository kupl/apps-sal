d = {0: 'midnight', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
     10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
     15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
     20: 'twenty', 30: 'half'}

for i in range(1, 10):
    d[20 + i] = f'{d[20]} {d[i]}'


def solve(time):
    h, m = [int(x) for x in time.split(':')]

    to = m > 30
    past_to = 'past to'.split()[to]
    if to:
        h += 1
        m = 60 - m

    h = h % 12 if h != 12 else h

    if m == 0:
        oc = ' o\'clock' if h else ''
        return f'{d[h]}{oc}'

    s = 's' if m > 1 else ''
    min_word = f' minute{s}' if m not in [15, 30] else ''

    minutes = d[m]
    hour = d[h]

    return f'{minutes}{min_word} {past_to} {hour}'

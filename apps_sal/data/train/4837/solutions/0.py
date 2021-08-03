RANGES = {
    'minute': (0, 59),
    'hour': (0, 23),
    'day of month': (1, 31),
    'month': (1, 12),
    'day of week': (0, 6),
}

ALIASES = {
    'month': ' JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC'.split(' '),
    'day of week': 'SUN MON TUE WED THU FRI SAT'.split(),
}


def get_alias(field, value):
    try:
        return ALIASES[field].index(value)
    except:
        return int(value)


def parse(crontab):
    def parse_field(field, value):
        values = set()
        for part in value.split(','):
            part, *end = part.split('/')
            step = int(end[0]) if end else 1
            if part == '*':
                start, stop = RANGES[field]
            else:
                part, *end = part.split('-')
                start = get_alias(field, part)
                stop = get_alias(field, end[0]) if end else start
            values.update(range(start, stop + 1, step))
        return ' '.join(map(str, sorted(values)))
    return '\n'.join(f'{field:<15}{parse_field(field, value)}'
                     for field, value in zip(RANGES, crontab.split()))

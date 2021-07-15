import re

WILDCARDS = {
    'minute': {
        'range': list(range(60))
    },
    'hour': {
        'range': list(range(24))
    },
    'day-of-month': {
        'range': list(range(1, 32))
    },
    'month': {
        'range': list(range(1, 13)),
        'names': {
            'JAN': 1,
            'FEB': 2,
            'MAR': 3,
            'APR': 4,
            'MAY': 5,
            'JUN': 6,
            'JUL': 7,
            'AUG': 8,
            'SEP': 9,
            'OCT': 10,
            'NOV': 11,
            'DEC': 12
        }
    },
    'day-of-week': {
        'range': list(range(7)),
        'names': {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 0}
    }
}

def parse_interval(interval, type):
    rng = WILDCARDS[type]['range']
    substitutes = WILDCARDS[type].get('names', {})

    for k, v in substitutes.items():
        interval = interval.replace(k, str(v))

    interval = interval.replace('*', '{}-{}'.format(rng[0], rng[-1]))
    return range_parser(interval)

def parse(crontab):
    (minute, hour, day_month, month, day_week) = crontab.split(' ')

    out = [
        ['minute', parse_interval(minute, 'minute')], 
        ['hour', parse_interval(hour, 'hour')], 
        ['day of month', parse_interval(day_month, 'day-of-month')], 
        ['month', parse_interval(month, 'month')], 
        ['day of week', parse_interval(day_week, 'day-of-week')]
    ]

    return format(out)


def format(cron_conf):
    """Formats results"""
    out = []
    for item in cron_conf:
        out += ["{}{}".format(str.ljust(item[0], 15), ' '.join(map(str, item[1])))]
    return '\n'.join(out)

def range_parser(range_spec):
    """Expands the range range_spec into list"""
    range_list = []
    ranges = re.split(r'\s?,\s?', range_spec)

    for rng in ranges:
        out = parse_range(rng)
        range_list += out

    return sorted(range_list)

def parse_range(rng):
    spec = re.split(r'-|/', rng)
    spec = [int(s) for s in spec]

    if len(spec) == 1:
        return [spec[0]]
    elif len(spec) == 2:
        return list(range(spec[0], spec[1] + 1))
    elif len(spec) == 3:
        return list(range(spec[0], spec[1] + 1, spec[2]))

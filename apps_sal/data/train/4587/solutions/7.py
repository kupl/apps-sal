def clean(string):
    return string.replace("'", '')


def range_parser(string):
    l = []
    for elem in clean(string).split(','):
        if '-' in elem:
            l.extend(parse_range(elem))
        else:
            l.append(int(elem))
    return l


def parse_range(interval):
    step = 1
    if ':' in interval:
        (interval, step) = interval.split(':')
    (start, stop) = [int(e) for e in interval.split('-')]
    return list(range(start, stop + 1, int(step)))

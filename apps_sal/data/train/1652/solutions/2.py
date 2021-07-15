def f(n, unit):
    return [', ', '{} {}{}'.format(n, unit, 's' if n > 1 else '')]

def format_duration(seconds):
    if not seconds: return 'now'

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    fs = []
    if years: fs.extend(f(years, 'year'))
    if days: fs.extend(f(days, 'day'))
    if hours: fs.extend(f(hours, 'hour'))
    if minutes: fs.extend(f(minutes, 'minute'))
    if seconds: fs.extend(f(seconds, 'second'))

    fs[-2] = ' and '
    fs.pop(0)
    return ''.join(fs)

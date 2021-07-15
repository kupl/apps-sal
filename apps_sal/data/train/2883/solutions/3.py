def to_pretty(seconds):
    if seconds == 0:
        return 'just now'
    fmt = '{} {}{} ago'.format
    human = ((604800, 'week'), (86400, 'day'), (3600, 'hour'),
             (60, 'minute'), (1, 'second'))
    for num, word in human:
        quo, rem = divmod(seconds, num)
        if quo == 1:  # singular
            return fmt('an' if num == 3600 else 'a', word, '')
        elif quo > 0:
            return fmt(quo, word, 's')


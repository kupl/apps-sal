def to_pretty(seconds):
    if seconds == 0:
        return 'just now'
    elif seconds // (7 * 24 * 60 * 60):
        weeks = seconds // (7 * 24 * 60 * 60)
        extra = '' if weeks == 1 else 's'
        weeks = 'a' if weeks == 1 else weeks
        return '{} week{} ago'.format(weeks, extra)
    elif seconds // (24 * 60 * 60):
        days = seconds // (24 * 60 * 60)
        extra = '' if days == 1 else 's'
        days = 'a' if days == 1 else days
        return '{} day{} ago'.format(days, extra)
    elif seconds // (60 * 60):
        hours = seconds // (60 * 60)
        extra = '' if hours == 1 else 's'
        hours = 'an' if hours == 1 else hours
        return '{} hour{} ago'.format(hours, extra)
    elif seconds // 60:
        minutes = seconds // 60
        extra = '' if minutes == 1 else 's'
        minutes = 'a' if minutes == 1 else minutes
        return '{} minute{} ago'.format(minutes, extra)
    else:
        extra = '' if seconds == 1 else 's'
        seconds = 'a' if seconds == 1 else seconds
        return '{} second{} ago'.format(seconds, extra)

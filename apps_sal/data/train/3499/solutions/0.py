def to24hourtime(hour, minute, period):
    return '%02d%02d' % (hour % 12 + 12 * (period == 'pm'), minute)

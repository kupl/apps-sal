from time import gmtime, strftime


def day_and_time(mins):
    return strftime('%A %H:%M', gmtime(3600 * 24 * 3 + 60 * mins))

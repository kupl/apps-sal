def to_pretty(seconds):

    minutes = seconds // 60
    hours = seconds // 3600
    days = seconds // (3600 * 24)
    weeks = seconds // (3600 * 24 * 7)

    if weeks == 1:
        return "a week ago"
    if weeks > 1:
        return str(weeks) + " weeks ago"
    if days == 1:
        return "a day ago"
    if days > 1:
        return str(days) + " days ago"
    if hours == 1:
        return "an hour ago"
    if hours > 1:
        return str(hours) + " hours ago"
    if minutes == 1:
        return "a minute ago"
    if minutes > 1:
        return str(minutes) + " minutes ago"
    if seconds == 0:
        return "just now"
    if seconds == 1:
        return "a second ago"
    if seconds > 1:
        return str(seconds) + " seconds ago"
